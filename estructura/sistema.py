"""

 En cada sistema se tiene que definir el panel a usar y la tecnologia. Tiene como
objetivo armacenar la informacion espesifica de un SSFV.

"""

from mi_gestor_pickle import *
from panel import *
from hsp import *


def _buscar_en_listas(panel, tecnologia, zona):
    """
    Carga de los archivos .pkl guardados en la carpeta salva,se obtienen tres
    listas y se buscan en ellas los objetos especificados.

    :param panel: identificador del tipo de panel a usar.
    :param tecnologia: tecnolgia definida por el material.
    :param zona: zona en la que se hace el sistema, esta define la hsp(hora solar pico).
    :return:
    """

    paneles_list: list[Panel] = cargar_informacion_pickle("salva/Paneles")
    tecnologias_list: list[Tecnologia] = cargar_informacion_pickle("salva/Tecnologias")
    hsp_list: list[Hsp] = cargar_informacion_pickle("salva/Hsp")

    i = 0  # Posicion de la lista
    a, b, c = True, True, True  # Al estar en en False indica que ya se encontro el objeto
    # deseado, de lo contrario se debe seguir recorriendo la lista.
    p, t, z = None, None, None  # Aqui se almacena el objeto en caso de ser encontrado.

    while i < len(paneles_list) or i < len(tecnologias_list) or i < len(hsp_list):
        # Este ciclo tiene como condicion de parada cuando la variable i supere el tamanno
        # de las tres listas.

        # En cada una de las tres condicionales siguientes se verifica si la variable
        # i ya supero el tamanno de la lista para evitar errores de indice.
        if i < len(paneles_list) and a:
            if panel == paneles_list[i].identificador:
                p = paneles_list[i]
                a = False
                print("Encontro panel")

        if i < len(tecnologias_list) and b:
            if tecnologia == tecnologias_list[i].material:
                t = tecnologias_list[i]
                b = False
                print("Encontro tecnologia")

        if i < len(hsp_list) and c:
            if zona == hsp_list[i].zona:
                z = hsp_list[i]
                c = False
                print("Encontro zona")

        # Se compueba si las variables a, b y c estan en False, de ser asi
        # se cierra el ciclo ya que no es necesario seguir recorriendo las
        # listas.
        if not (a or b or c):
            break

        i += 1
        print("sigue")

    return p, t, z


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
        self.panel, self.tecnologia, self.zona = \
            _buscar_en_listas(panel, tecnologia, zona)


