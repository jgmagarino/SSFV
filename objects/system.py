"""

 En cada sistema se tiene que definir el panel a usar y la tecnologia. Tiene como
objetivo armacenar la informacion espesifica de un SSFV.

"""
from objects.json_manager import get_unic_value


class System:
    def __init__(self, name: str, panel: int, technology: str, place: str,
                 description: str = "No hay descripcion", progress: int = 0):
        """
        Al iniciar el sistema, busca el panel, la tecnologia y la zona especificada.

        :param name: Nombre unico para cada sistema.
        :param panel: identificador del tipo de panel a usar.
        :param technology: tecnolgia definida por el material.
        :param place: zona en la que se hace el sistema, esta define la hsp(hora solar pico).
        :param description: breeve descripcion donde se añadiran detalles del sistema.
        """
        self.name = name

        self.description = description

        self.progress = progress

        self.panel: dict = get_unic_value("../save/Panels.json",
                                          key="identificador",
                                          value=panel)
        self.technology: dict = get_unic_value("../save/Technologies.json",
                                               key="material",
                                               value=technology)
        self.place: dict = get_unic_value("../save/Hsp.json",
                                          key="zona",
                                          value=place)

        # Parametros del sistema que quedaran definidos a la hora de llamar las diferentes funciones.
        self.useful_energy = 0.0
        self.number_of_panels = 0
        self.area = 0.0
        self.cost = 0.0
        self.income = 0.0
        self.recovery_period = 0

    def calculate_useful_energy(self, power=None, available_area=None):
        """
        Se calcula a partir de la potencia que se desea en un sistema y la hsp de la zona

        :param available_area: En caso de que se tenga un area limitada, de lo contrario es None.
        :param power: potencia a instalar en el sistema.
        """

        if available_area is not None:
            self.area = available_area
            self.number_of_panels = available_area / 1.4 * self.technology["area"]
            power = self.number_of_panels * self.panel["potencia_pico"]

        self.useful_energy = power * self.place["valor"]
        return self.useful_energy

    def calculate_number_of_panels(self):
        """
        Calcula el numero de paneles que se debe instalar en el sistema teniendo la energia
        util que se requiere, esta debe ser previamente calculada.
        """

        if self.useful_energy == 0.0:
            print("Se necesita la energia util para calcular el numero de paneles")
        else:
            aux = 0.654 * self.place["valor"] * self.panel["potencia_pico"]  # Energia que genera un panel en esta zona.
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
            self.area = self.number_of_panels * self.panel["area"]
            self.area = self.area * 1.4 if al_sur else self.area

            return self.area

    def calculate_cost(self, additional_cost: bool = True):
        """
        Calculo de costo del sistema, tiene que ser calculado previamente la cantidad
        de paneles a usar.

        :param additional_cost: inicializa por defecto en True, indica que se debe sumar
        un 30% del costo de los paneles al costo total.
        """
        if self.number_of_panels == 0:
            print("Se tiene que calcular el numero de paneles.")
        else:

            self.cost = self.number_of_panels * self.panel["precio"]
            self.cost += self.cost * (3 / 10) if additional_cost else 0

            return self.cost

    def calculate_income(self):
        """
        Calculo del ingreso generado por el sistema en un año, tiene que ser previamente
        calculada la energia util por dia del sistema.
        """
        self.income = 365 * self.useful_energy * self.panel["precio_kwh_sen"]

    def calculate_recovery_period(self):
        """
        Periodo de recuperacion de la invercion en años.
        """
        self.recovery_period = self.cost / self.income
        return self.recovery_period

    @property
    def __dict__(self):
        return {
            "name": self.name,
            "panel": self.panel,
            "technology": self.technology,
            "place": self.place,
            "useful_energy": self.useful_energy,
            "number_of_panels": self.number_of_panels,
            "area": self.area,
            "cost": self.cost,
            "income": self.income,
            "recovery_period": self.recovery_period,
            "description": self.description,
            "progress": self.progress
        }


def from_dict(system: dict):
    new_system = System(
        name=system["name"],
        panel=system["panel"][0]["identificador"],
        technology=system["technology"][0]["material"],
        place=system["place"][0]["zona"],
        description=system["description"],
        progress=system["progress"]
    )

    new_system.useful_energy = system["useful_energy"]
    new_system.number_of_panels = system["number_of_panels"]
    new_system.area = system["area"]
    new_system.cost = system["cost"]
    new_system.income = system["income"]
    new_system.recovery_period = system["recovery_period"]

    return new_system

