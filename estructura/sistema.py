"""

 En cada sistema se tiene que definir el panel a usar y la tecnologia. Tiene como
objetivo armacenar la informacion espesifica de un SSFV.

"""

from mi_gestor_pickle import *
from panel import *
from hsp import *


class Sistema:
    def __init__(self, panel, tecnologia, zona):
        self._buscar_en_listas(panel, tecnologia, zona)

    def _buscar_en_listas(self, panel, tecnologia, zona):
        list_paneles: list[Panel] = cargar_informacion_pickle("salva/Paneles")
        list_tecnologias: list[Tecnologia] = cargar_informacion_pickle("salva/Tecnologias")
        list_hsp: list[Hsp] = cargar_informacion_pickle("salva/Hsp")

        i = 0
        a, b, c = True, True, True

        while i > len(list_paneles) and i > len(list_tecnologias) and i > len(list_hsp):
            if i < len(list_paneles) and a:
                if panel == list_paneles[i].identificador:
                    self.panel = list_paneles[i]
                    a = False

            if i < len(list_tecnologias) and b:
                if tecnologia == list_tecnologias[i].material:
                    self.tecnologia = list_tecnologias[i]
                    b = False

            if i < len(list_hsp) and c:
                if zona == list_hsp[i].zona:
                    self.zona = list_hsp[i]
                    c = False

            if not a and not b and not c:
                break
