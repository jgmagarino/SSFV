"""

 En cada sistema se tiene que definir el panel a usar y la tecnologia. Tiene como
objetivo armacenar la informacion espesifica de un SSFV.

"""

from objects.panel import Panel
from objects.hsp import Hsp
from objects.technology import Technology


class System:
    def __init__(self, name: str, panel: Panel, technology: Technology, hsp: Hsp,
                 description: str = "No hay descripcion", progress: int = 0):
        """
        Al iniciar el sistema, busca el panel, la tecnologia y la zona especificada.

        :param name: Nombre unico para cada sistema.
        :param panel: identificador del tipo de panel a usar.
        :param technology: tecnolgia definida por el material.
        :param hsp: zona en la que se hace el sistema, esta define la hsp(hora solar pico).
        :param description: breeve descripcion donde se añadiran detalles del sistema.
        :param progress: estado en el que se encuentra el sistema, 0 - en planificacion, 1 - en construccion y  2 - terminado
        """
        self.name = name

        self.description = description

        self.progress = progress

        self.panel = panel
        self.technology = technology
        self.hsp = hsp

        # Parametros del sistema que quedaran definidos a la hora de llamar las diferentes funciones.
        self.useful_energy = 0.0
        self.number_of_panels = 0
        self.area = 0.0


    def calculate_useful_energy(self, power=None, available_area=None):
        """
        Se calcula a partir de la potencia que se desea en un sistema y la hsp de la zona

        :param available_area: En caso de que se tenga un area limitada, de lo contrario es None.
        :param power: potencia a instalar en el sistema.
        """

        if available_area is not None:
            self.area = available_area
            self.number_of_panels = available_area / 1.4 * self.technology.surface
            power = self.number_of_panels * self.panel.peak_power

        self.useful_energy = power * self.hsp.value
        return self.useful_energy, self.area, self.number_of_panels

    def calculate_number_of_panels(self):
        """
        Calcula el numero de paneles que se debe instalar en el sistema teniendo la energia
        util que se requiere, esta debe ser previamente calculada.
        """

        if self.useful_energy == 0.0:
            print("Se necesita la energia util para calcular el numero de paneles")
        else:
            aux = 0.654 * self.hsp.value * self.panel.peak_power  # Energia que genera un panel en esta zona.
            self.number_of_panels = (self.useful_energy / aux) + 1
            return self.number_of_panels

    def calculate_area(self, al_sur: bool = True):
        """
        Calcula el area requerida para un numero de paneles especifico que tiene que ser previamente
        calculado.

        :param al_sur: indica si estan orientados al sur, toma True como valor por defecto.
        """

        if self.number_of_panels == 0:
            print("Error: aun no se tiene el numero de paneles para calcular el area...")
        else:
            self.area = self.number_of_panels * self.panel.area
            self.area = self.area * 1.4 if al_sur else self.area

            return self.area


