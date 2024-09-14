"""

 En cada sistema se tiene que definir el panel a usar y la tecnologia. Tiene como
objetivo armacenar la informacion espesifica de un SSFV.

"""
from platform import system

import objects.db_querys as db
from objects.panel import Panel
from objects.hsp import Hsp
from objects.technology import Technology


class System:
    def __init__(self, name: str, id_panel: str, pleace: str,
                 description: str = "No hay descripcion", progress: int = 0, visible: int = 1):
        """
        Al iniciar el sistema, busca el panel, la tecnologia y la zona especificada.

        :param name: Nombre unico para cada sistema.
        :param id_panel: identificador del tipo de panel a usar.
        :param pleace: zona en la que se hace el sistema, esta define la hsp(hora solar pico).
        :param description: breeve descripcion donde se añadiran detalles del sistema.
        :param progress: estado en el que se encuentra el sistema, 0 - en planificacion, 1 - en construccion y  2 - terminado
        :param visible: indica si esta en la papelera de reciclage (0) o no (1)
        """
        self.name = name

        self.description = description

        self.visible = visible

        self.progress = progress

        self.panel: Panel = db.get_panel(id_panel)

        self.hsp: Hsp = db.get_hsp(pleace)



