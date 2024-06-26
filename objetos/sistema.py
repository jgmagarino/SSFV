"""

 En cada sistema se tiene que definir el panel a usar y la tecnologia. Tiene como
objetivo armacenar la informacion espesifica de un SSFV.

"""

from funciones import gestor_json as jsn
import objetos_segundarios as obj


def _buscar_en_listas(panel_param: int, tecnologia_param: str, zona_param: str) -> tuple[dict, dict, dict]:
    """
    Carga de los archivos .pkl guardados en la carpeta salva,se obtienen tres
    listas y se buscan en ellas los objetos especificados.

    :param panel_param: identificador del tipo de panel a usar.
    :param tecnologia_param: tecnolgia definida por el material.
    :param zona_param: zona en la que se hace el sistema, esta define la hsp(hora solar pico).
    :return:
    """

    panel = None
    tecnologia = None
    hsp = None

    paneles: list[dict] = jsn.cargar("../salva/Paneles.json")
    hsps: list[dict] = jsn.cargar("../salva/Hsp.json")
    tecnologias: list[dict] = jsn.cargar("../salva/Tecnologias.json")

    for p in paneles:
        if panel_param == p["identificador"]:
            panel = p
            print(f"encontro el panel {p}")

    for t in tecnologias:
        if tecnologia_param == t["material"]:
            tecnologia = t
            print(f"encontro la tecnologia {t}")

    for h in hsps:
        if zona_param == h["zona"]:
            hsp = h
            print(f"encontro la hsp {h}")

    return panel, tecnologia, hsp


class Sistema:
    def __init__(self, nombre_sistema: str, panel: int, tecnologia: str, zona: str):
        """
        Al inicializar el sistema hace uso de la funcion privada _buscar_en_listas
        para dado los tres parametros buscar en la lista de paneles, la lista de hsp
        y la lista de tecnologias, los objetos a usar en especifico.

        :param panel: identificador del tipo de panel a usar.
        :param tecnologia: tecnolgia definida por el material.
        :param zona: zona en la que se hace el sistema, esta define la hsp(hora solar pico).
        """
        self.nombre_sistema = nombre_sistema

        resultado = _buscar_en_listas(panel, tecnologia, zona)

        self.panel: dict = resultado[0]
        self.tecnologia: dict = resultado[1]
        self.zona: dict = resultado[2]

        # Parametros del sistema que quedaran definidos a la hora de llamar las diferentes funciones.
        self.energia_util = 0.0
        self.numero_de_paneles = 0
        self.area = 0.0
        self.costo = 0.0
        self.ingreso = 0.0
        self.periodo_de_recuperacion = 0

    def energia_util_requerida_def(self, potencia):
        """
        Se calcula a partir de la potencia que se decea en un sistema y la hsp de la zona

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

        return potencia * self.zona["valor"]

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
                self.area = 1.4 * self.numero_de_paneles * self.tecnologia["area"]
            else:
                self.area = self.numero_de_paneles * self.tecnologia["area"]

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
            "periodo_de_recuperacion": self.periodo_de_recuperacion
        }


"Datos de prueba"

hsp_list = [obj.crear_hsp("Cienfuegos", 1),
            obj.crear_hsp("Villa Clara", 2),
            obj.crear_hsp("La Habana", 3)]

panel_list = [obj.crear_panel(1, 1, 1, 1),
              obj.crear_panel(2, 1, 1, 1),
              obj.crear_panel(3, 1, 1, 1)]

tecnologia_list = [obj.crear_tecnologia("silicio", 5),
                   obj.crear_tecnologia("ormigon", 6),
                   obj.crear_tecnologia("peline", 7)]

jsn.guardar("../salva/Hsp.json", hsp_list)
jsn.guardar("../salva/Paneles.json", panel_list)
jsn.guardar("../salva/Tecnologias.json", tecnologia_list)

sistema_list = [Sistema("Sistema Cienfuegos", 1, "silicio", "Cienfuegos"),
                Sistema("Sistema Villa Clara", 2, "ormigon", "Villa Clara"),
                Sistema("Sistema La Habana", 3, "peline", "La Habana")]

aux_sistema = []

for i in sistema_list:
    aux_sistema.append(i.__dict__)

jsn.guardar("../salva/Sistemas.json", aux_sistema)

a = jsn.cargar("../salva/Sistemas.json")

print(a)
