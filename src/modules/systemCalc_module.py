from src.database.db_connection import DbConnection
from src.modules.system_module import System
import math
from src.modules.technology_module import Technology


class SystemCalc:
    """Clase que referencia a los calculos del sistema"""

    def __init__(self, system: System):
        """

        :param system: Sistema al cual se le va a ejecutar los calculos
        """
        self.__peak_power = 0
        self.__number_of_panels = 0
        self.__area = 0
        self.__useful_energy = 0
        self.__system = system

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, value):
        self.__system = value

    @property
    def peak_power(self):
        return self.__peak_power

    @peak_power.setter
    def peak_power(self, new_peak_power):
        self.__peak_power = new_peak_power

    @property
    def area(self) -> int:
        return self.__area

    @area.setter
    def area(self, new_area):
        self.__area = new_area

    @property
    def useful_energy(self):
        return self.__useful_energy

    @useful_energy.setter
    def useful_energy(self, value):
        self.__useful_energy = value

    @property
    def number_of_panels(self):
        return self.__number_of_panels

    @number_of_panels.setter
    def number_of_panels(self, value):
        self.__number_of_panels = value

    def save(self) -> bool:
        db = DbConnection()
        db.connect()

        query = """INSERT INTO SystemCalc (system_name, useful_energy, number_of_panel, area, peak_power) 
                                                    VALUES (?, ?, ?, ?, ?)"""

        db.execute_query(query, [self.__system.name, self.__useful_energy,
                                 self.__number_of_panels, self.__area, self.__peak_power])
        return True

    def delete(self):
        db = DbConnection()
        db.connect()

        db.delete_row('SystemCalc', "system_name", self.__system.name)
        return True


# -------------------------------------------------------------------------------------------------------------


class SystemCalcPeakPower(SystemCalc):
    """Clase que referencia a los calculos del sistema en funcion de el area requerida"""

    def __init__(self, system: System, surface_available: float):
        super().__init__(system)
        self.__surface_available = float(surface_available)
        self.area = surface_available

    def approx_peak_power(self, worst_case: bool) -> float:
        """Calcula la potencia pico aproximada del sistema en dependencia si se toma el peor o mejor caso
        del valor del area de la tecnologia determinada"""

        panel_id = self.system.panel_id
        db = DbConnection()
        db.connect()

        query1 = f"""SELECT cell_material FROM Panel WHERE panel_id = ?"""
        technology_material = db.execute_query_one(query1, [panel_id])[0]

        query2 = f"""SELECT surface FROM Technology WHERE material = ?"""
        technology_surface = db.execute_query_one(query2, [technology_material])[0]

        technology = Technology(technology_material, technology_surface)
        db.close()
        if not worst_case:
            return self.__surface_available / technology.convert_to_number()[0]
        return self.__surface_available / technology.convert_to_number()[1]

    def num_panels(self) -> int:
        """Calcula el numero de paneles del sistema"""
        panel_id = self.system.panel_id
        db = DbConnection()
        db.connect()

        query = """SELECT area from Panel WHERE panel_id = ?"""
        panel_area = db.execute_query_one(query, [panel_id])[0]

        self.number_of_panels = math.ceil(self.__surface_available / panel_area)
        return math.ceil(self.__surface_available / panel_area)

    def calc_peak_power(self) -> float:
        """Calcula la potencia pico a intalar en el sistema"""
        panel_id = self.system.panel_id
        db = DbConnection()
        db.connect()

        query = """SELECT peak_power from Panel WHERE panel_id = ?"""
        panel_power = db.execute_query_one(query, [panel_id])[0]

        if not self.system.to_south:
            result1 = 0.8 * self.num_panels() * panel_power
            self.peak_power = result1
            return result1
        else:
            result2 = self.num_panels() / 1.4 * panel_power
            self.peak_power = result2
            return result2

    def calc_useful_energy(self):
        """Calcula la energia util del sistema"""
        place = self.system.place
        db = DbConnection()
        db.connect()

        query = """SELECT value FROM Hsp WHERE place = ?"""
        hsp = db.execute_query_one(query, [place])[0]

        result = self.calc_peak_power() * hsp
        self.useful_energy = result
        return result

    def validate(self) -> bool:
        """Valida si el area disponible para el sistema es de valor numerico"""
        return isinstance(self.__surface_available, (int, float))


# -------------------------------------------------------------------------------------------------------------


class SystemCalcArea(SystemCalc):
    """Clase que referencia a los calculos del sistema en funcion de la potencia pico a instalar"""

    def __init__(self, system: System, peak_powwer: float):
        super().__init__(system)
        self.__peak_power = float(peak_powwer)
        self.peak_power = peak_powwer

    def approx_required_surface(self, worst_case: bool) -> float:
        """Calcula el area requerida aproximada del sistema en dependencia si se toma el peor o mejor caso
            del valor del area de la tecnologia determinada"""
        panel_id = self.system.panel_id

        db = DbConnection()
        db.connect()

        query1 = """SELECT cell_material FROM Panel WHERE panel_id = ?"""
        technology_material = db.execute_query_one(query1, [panel_id])[0]

        query2 = """SELECT surface FROM Technology WHERE material = ?"""
        technology_surface = db.execute_query_one(query2, [technology_material])[0]
        technology = Technology(technology_material, technology_surface)

        if not worst_case:
            return self.__peak_power * technology.convert_to_number()[0]
        return self.__peak_power * technology.convert_to_number()[1]

    def calc_useful_energy(self) -> float:
        """Calcula la energia util del sistema"""
        place = self.system.place

        db = DbConnection()
        db.connect()

        query = """SELECT value FROM Hsp WHERE place = ?"""
        hsp = db.execute_query_one(query, [place])[0]

        result = self.__peak_power * hsp
        self.useful_energy = result
        return result

    def num_panels(self) -> int:
        """Calcula el numero de paneles del sistema"""
        panel_id = self.system.panel_id
        place = self.system.place

        db = DbConnection()
        db.connect()

        query1 = """SELECT peak_power FROM Panel WHERE panel_id = ?"""
        panel_power = db.execute_query_one(query1, [panel_id])[0]

        query2 = """SELECT value FROM Hsp WHERE place = ?"""
        hsp = db.execute_query_one(query2, [place])[0]

        result = (round((self.calc_useful_energy() / 0.654) * hsp * panel_power)) + 1
        self.number_of_panels = result
        return result

    def calc_required_surface(self):
        """Calcula el area requerida para el sistema"""
        panel_id = self.system.panel_id
        db = DbConnection()
        db.connect()

        query = """SELECT area from Panel WHERE panel_id = ?"""
        panel_area = db.execute_query_one(query, [panel_id])[0]

        if not self.system.to_south:
            result = self.num_panels() * panel_area
            self.area = result
            return result
        else:
            result = 1.4 * self.num_panels() * panel_area
            self.area = result
            return result

    def validate(self) -> bool:
        """Valida si la potencia pico a instalar es de valor numerico"""
        return isinstance(self.__peak_power, (int, float))
