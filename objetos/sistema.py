"""

 En cada sistema se tiene que definir el panel a usar y la tecnologia. Tiene como
objetivo armacenar la informacion espesifica de un SSFV.

"""
from objetos.json_manager import get_unic_value


class Sistema:
    def __init__(self, nombre_sistema: str, panel: int, tecnologia: str, zona: str,
                 descripcion: str = "No hay descripcion", progress: int = 0):
        """
        Al iniciar el sistema, busca el panel, la tecnologia y la zona especificada.

        :param nombre_sistema: Nombre unico para cada sistema.
        :param panel: identificador del tipo de panel a usar.
        :param tecnologia: tecnolgia definida por el material.
        :param zona: zona en la que se hace el sistema, esta define la hsp(hora solar pico).
        """
        self.nombre_sistema = nombre_sistema

        self.descripcion = descripcion

        self.progress = progress

        self.panel: dict = get_unic_value("../salva/Paneles.json",
                                          key="identificador",
                                          value=panel)
        self.tecnologia: dict = get_unic_value("../salva/Tecnologias.json",
                                               key="material",
                                               value=tecnologia)
        self.zona: dict = get_unic_value("../salva/Hsp.json",
                                         key="zona",
                                         value=zona)

        # Parametros del sistema que quedaran definidos a la hora de llamar las diferentes funciones.
        self.energia_util = 0.0
        self.numero_de_paneles = 0
        self.area = 0.0
        self.costo = 0.0
        self.ingreso = 0.0
        self.periodo_de_recuperacion = 0

    def energia_util_requerida_def(self, potencia):
        """
        Se calcula a partir de la potencia que se desea en un sistema y la hsp de la zona

        :param potencia: potencia a instalar en el sistema.
        """

        self.energia_util = potencia * self.zona["valor"]
        return self.energia_util

    def energia_util_disponible(self, area_disponible):
        """
        A partir del area disponible se calcula el numero de paneles que se puede usar,
        la potencia pico que tendra y posteriormente la energia util que generara el sistema.

        :param area_disponible: area disponible para hacer el sistema
        """
        self.area = area_disponible
        self.numero_de_paneles = area_disponible / 1.4 * self.tecnologia["area"]

        potencia = self.numero_de_paneles * self.panel["potencia_pico"]

        self.energia_util = potencia * self.zona["valor"]

        return self.energia_util

    def numero_de_paneles_def(self):
        """
        Calcula el numero de paneles que se debe instalar en el sistema teniendo la energia
        util que se requiere, esta debe ser previamente calculada.
        """

        if self.energia_util == 0.0:
            print("Se necesita la energia util para calcular el numero de paneles")
        else:
            aux = 0.654 * self.zona["valor"] * self.panel["potencia_pico"]  # Energia que genera un panel en esta zona.
            self.numero_de_paneles = (self.energia_util / aux) + 1
            return self.numero_de_paneles

    def area_requerida_def(self, al_sur: bool = True):
        """
        Calcula el area requerida para un numero de paneles especifico que tiene que ser previamente
        calculado.

        :param al_sur: indica si estan orientados al sur, toma True como valor por defecto.
        """

        if self.numero_de_paneles == 0:
            print("Se necesita el numero de paneles para obtener el area requerida")
        else:
            if al_sur:
                self.area = 1.4 * self.numero_de_paneles * self.panel["area"]
            else:
                self.area = self.numero_de_paneles * self.panel["area"]

            return self.area

    def costo_def(self, costo_adicional: bool = True):
        """
        Calculo de costo del sistema, tiene que ser calculado previamente la cantidad
        de paneles a usar.

        :param costo_adicional: inicializa por defecto en True, indica que se debe sumar
        un 30% del costo de los paneles al costo total.
        """
        if self.numero_de_paneles == 0:
            print("Se tiene que calcular el numero de paneles.")
        else:
            if costo_adicional:
                self.costo = self.numero_de_paneles * self.panel["precio"]
                self.costo += self.costo * (3 / 10)
            else:
                self.costo = self.numero_de_paneles * self.panel["precio"]

            return self.costo

    def ingreso_def(self):
        """
        Calculo del ingreso generado por el sistema en un anno, tiene que ser previamente
        calculada la energia util por dia del sistema.
        """
        self.ingreso = 365 * self.energia_util * self.panel["precio_kwh_sen"]

    def periodo_de_recuperacion_def(self):
        """
        Periodo de recuperacion de la invercion en años.
        """
        self.periodo_de_recuperacion = self.costo / self.ingreso
        return self.periodo_de_recuperacion

    @classmethod
    def desde_diccionario(cls, diccionario: dict):
        return cls(**diccionario)

    @property
    def __dict__(self):
        return {
            "nombre_sistema": self.nombre_sistema,
            "panel": self.panel,
            "tecnologia": self.tecnologia,
            "zona": self.zona,
            "energia_util": self.energia_util,
            "numero_de_paneles": self.numero_de_paneles,
            "area": self.area,
            "costo": self.costo,
            "ingreso": self.ingreso,
            "periodo_de_recuperacion": self.periodo_de_recuperacion,
            "descripcion": self.descripcion
        }


def dict_to_sistema(sistema: dict):
    new_sistema = Sistema(
        nombre_sistema=sistema["nombre_sistema"],
        panel=sistema["panel"][0]["identificador"],
        tecnologia=sistema["tecnologia"][0]["material"],
        zona=sistema["zona"][0]["zona"],
        descripcion=sistema["descripcion"],
        progress=sistema["progress"]
    )

    new_sistema.energia_util = sistema["energia_util"]
    new_sistema.numero_de_paneles = sistema["numero_de_paneles"]
    new_sistema.area = sistema["area"]
    new_sistema.costo = sistema["costo"]
    new_sistema.ingreso = sistema["ingreso"]
    new_sistema.periodo_de_recuperacion = sistema["periodo_de_recuperacion"]

    return new_sistema

