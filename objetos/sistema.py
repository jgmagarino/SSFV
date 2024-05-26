"""

 En cada sistema se tiene que definir el panel a usar y la tecnologia. Tiene como
objetivo armacenar la informacion espesifica de un SSFV.

"""

from funciones import gestor_json as jsn
from hsp import *
from panel import *


def _buscar_en_listas(panel, tecnologia, zona) -> tuple[Panel, Tecnologia, Hsp]:
    """
    Carga de los archivos .pkl guardados en la carpeta salva,se obtienen tres
    listas y se buscan en ellas los objetos especificados.

    :param panel: identificador del tipo de panel a usar.
    :param tecnologia: tecnolgia definida por el material.
    :param zona: zona en la que se hace el sistema, esta define la hsp(hora solar pico).
    :return:
    """

    p = None
    t = None
    h = None

    paneles = jsn.cargar("../salva/Paneles.json")
    hsps = jsn.cargar("../salva/Hsp.json")
    tecnologias = jsn.cargar("../salva/Tecnologias.json")

    for i in paneles:
        if panel == i["identificador"]:
            p = Panel.desde_diccionario(i)
            print(f"encontro el panel {i}")

    for i in tecnologias:
        if tecnologia == i["material"]:
            t = Tecnologia.desde_diccionario(i)
            print(f"encontro la tecnologia {i}")

    for i in hsps:
        if zona == i["zona"]:
            h = Hsp.desde_diccionario(i)
            print(f"encontro la hsp {i}")

    return p, t, h


class Sistema:
    def __init__(self, panel: int, tecnologia: str, zona: str):
        """
        Al inicializar el sistema hace uso de la funcion privada _buscar_en_listas
        para dado los tres parametros buscar en la lista de paneles, la lista de hsp
        y la lista de tecnologias, los objetos a usar en especifico.

        :param panel: identificador del tipo de panel a usar.
        :param tecnologia: tecnolgia definida por el material.
        :param zona: zona en la que se hace el sistema, esta define la hsp(hora solar pico).
        """
        resultado = _buscar_en_listas(panel, tecnologia, zona)

        self.panel: Panel = resultado[0]
        self.tecnologia: Tecnologia = resultado[1]
        self.zona: Hsp = resultado[2]

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

        self.energia_util = potencia * self.zona.valor
        return self.energia_util

    def energia_util_disponible(self, area_disponible):
        """
        A partir del area disponible se calcula el numero de paneles que se puede usar,
        la potencia pico que tendra y posteriormente la energia util que generara el sistema.

        :param area_disponible: area disponible para hacer el sistema
        """
        self.area = area_disponible
        self.numero_de_paneles = area_disponible / 1.4 * self.tecnologia.area

        potencia = self.numero_de_paneles * self.panel.potencia_pico

        self.energia_util = potencia * self.zona.valor

        return potencia * self.zona.valor

    def numero_de_paneles_def(self):
        """
        Calcula el numero de paneles que se debe instalar en el sistema teniendo la energia
        util que se requiere, esta debe ser previamente calculada.
        """

        if self.energia_util == 0.0:
            print("Se necesita la energia util para calcular el numero de paneles")
        else:
            aux = 0.654 * self.zona.valor * self.panel.potencia_pico  # Energia que genera un panel en esta zona.
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
                self.area = 1.4 * self.numero_de_paneles * self.tecnologia.area
            else:
                self.area = self.numero_de_paneles * self.tecnologia.area

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
                self.costo = self.numero_de_paneles * self.panel.precio
                self.costo += self.costo * (3 / 10)
            else:
                self.costo = self.numero_de_paneles * self.panel.precio

            return self.costo

    def ingreso_def(self):
        """
        Calculo del ingreso generado por el sistema en un anno, tiene que ser previamente
        calculada la energia util por dia del sistema.
        """
        self.ingreso = 365 * self.energia_util * self.panel.precio_kwh_sen

    def periodo_de_recuperacion_def(self):
        """
        Periodo de recuperacion de la invercion en annos.
        """
        self.periodo_de_recuperacion = self.costo / self.ingreso
        return self.periodo_de_recuperacion

    @classmethod
    def desde_diccionario(cls, diccionario):
        return cls(**diccionario)

    @property
    def __dict__(self):
        return {
            "panel": self.panel.identificador,
            "tecnologia": self.tecnologia.material,
            "zona": self.zona.zona,
            "energia_util": self.energia_util,
            "numero_de_paneles": self.numero_de_paneles,
            "area": self.area,
            "costo": self.costo,
            "ingreso": self.ingreso,
            "periodo_de_recuperacion": self.periodo_de_recuperacion
        }


"Datos de prueba"

# hsp_list = [Hsp("Cienfuegos", 1),
#             Hsp("Villa Clara", 2),
#             Hsp("La Habana", 3)]
#
# panel_list = [Panel(1, 1, 1, 1),
#               Panel(2, 1, 1, 1),
#               Panel(3, 1, 1, 1)]
#
# tecnologia_list = [Tecnologia("silicio", 5),
#                    Tecnologia("ormigon", 6),
#                    Tecnologia("peline", 7)]
#
# aux_hsp = []
#
# for i in hsp_list:
#     aux_hsp.append(i.__dict__)
#
# aux_tecnologia = []
#
# for i in tecnologia_list:
#     aux_tecnologia.append(i.__dict__)
#
# aux_panel = []
#
# for i in panel_list:
#     aux_panel.append(i.__dict__)
#
# jsn.guardar("../salva/Hsp.json", aux_hsp)
# jsn.guardar("../salva/Paneles.json", aux_panel)
# jsn.guardar("../salva/Tecnologias.json", aux_tecnologia)

sistema_list = [Sistema(1, "silicio", "Cienfuegos"),
                Sistema(2, "ormigon", "Villa Clara"),
                Sistema(3, "peline", "La Habana")]

aux_sistema = []

for i in sistema_list:
    aux_sistema.append(i.__dict__)

jsn.guardar("../salva/Sistemas.json", aux_sistema)

a = jsn.cargar("../salva/Paneles.json")

print(a)
