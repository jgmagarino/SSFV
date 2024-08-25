import sqlite3

from objects.panel import Panel
from objects.hsp import Hsp
from objects.technology import Technology
from objects.system import System
from objects.economic_calc import EconomicCalc


class DatabaseConnection:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print("Se creo una coneccion con la base de datos")
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect('save/db_ssfv.db', check_same_thread=False)
        return cls._instance

    def query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    "---------------------------------------------"
    "Operaciones de insertar, eliminar y modificar"
    "---------------------------------------------"

    def insert_hsp(self, hsp: Hsp):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Hsp (place, value) VALUES (?, ?);",
                       (
                           hsp.place,
                           hsp.value)
                       )
        self.connection.commit()

    def insert_panel(self, panel: Panel):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Panel (id_panel, peak_power, cell_material, "
                       "area, price, price_kwh_sen) "
                       "VALUES (?, ?, ?, ?, ?, ?);",
                       (
                            panel.id_panel,
                            panel.peak_power,
                            panel.cell_material,
                            panel.area,
                            panel.price,
                            panel.price_kwh_sen)
                       )
        self.connection.commit()

    def insert_technology(self, technology: Technology):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Technology (technology, surface) "
                       "VALUES (?, ?);",
                       (
                           technology.technology,
                           technology.surface)
                       )
        self.connection.commit()

    def insert_economic_calc(self, economic_calc: EconomicCalc):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO EconomicCalc (name_system, cost, income, recovery_period)"
                       "VALUES (?, ?, ?, ?);",
                       (
                            economic_calc.system.name,
                            economic_calc.cost,
                            economic_calc.income,
                            economic_calc.recovery_period
                            )
                        )
        self.connection.commit()

    def insert_system(self, system: System, economic_calc: EconomicCalc=None):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO System (name, progress, description, id_panel,"
                       " technology, place, useful_energy, number_of_panels, area) "
                       "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);",
                       (
                            system.name,
                            system.progress,
                            system.description,
                            system.panel.id_panel,
                            system.technology.technology,
                            system.hsp.place,
                            system.useful_energy,
                            system.number_of_panels,
                            system.area
                            )
                       )

        if economic_calc is not None: self.insert_economic_calc(economic_calc)

        self.connection.commit()

    def get_all_panels(self) -> list[Panel]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Panel")

        panels = [Panel(*i) for i in cursor.fetchall()]

        return panels

    def get_all_hsp(self) -> list[Hsp]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Hsp")

        hsp = [Hsp(*i) for i in cursor.fetchall()]

        return hsp

    def get_all_technologies(self) -> list[Technology]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Technology")

        technologies = [Technology(*i) for i in cursor.fetchall()]

        return technologies

    def get_all_systems(self) -> list[System]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM System")

        systems = [System(*i) for i in cursor.fetchall()]

        return systems

    def get_all_economic_calcs(self) -> list[EconomicCalc]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM EconomicCalc")

        economic_calcs = [EconomicCalc(*i) for i in cursor.fetchall()]

        return economic_calcs

    def get_panel(self, id_panel: str) -> Panel:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Panel WHERE id_panel = ?",
                       (id_panel,))

        return Panel(*cursor.fetchone())

    def get_hsp(self, place: str) -> Hsp:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Hsp WHERE place = ?",
                       (place,))

        return Hsp(*cursor.fetchone())

    def get_technology(self, technology: str) -> Technology:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Technology WHERE technology = ?",
                       (technology,))

        return Technology(*cursor.fetchone())

    def get_system(self, name: str) -> System:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM System WHERE name = ?", (name,))

        return System(*cursor.fetchone())

    def get_economic_calc(self, system_name: str) -> EconomicCalc:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM EconomicCalc WHERE name = ?", (system_name,))

        return EconomicCalc(*cursor.fetchone())

    def delete_all_panels(self):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Panel")
        self.connection.commit()

    def delete_all_hsp(self):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Hsp")
        self.connection.commit()

    def delete_all_technologies(self):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Technology")
        self.connection.commit()

    def delete_all_systems(self):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM System")
        self.connection.commit()

    def delete_all_economic_calcs(self):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM EconomicCalc")
        self.connection.commit()

    def delete_panel(self, id_panel: str) -> Panel:
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Panel WHERE id_panel = ?", (id_panel,))
        self.connection.commit()
        return Panel(*cursor.fetchone())

    def delete_hsp(self, place: str) -> Hsp:
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Hsp WHERE place = ?", (place,))
        self.connection.commit()
        return Hsp(*cursor.fetchone())

    def delete_technology(self, technology: str) -> Technology:
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Technology WHERE technology = ?", (technology,))
        self.connection.commit()
        return Technology(*cursor.fetchone())

    def delete_system(self, system_name: str) -> System:
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM System WHERE name = ?", (system_name,))
        self.delete_economic_calc(system_name)
        self.connection.commit()
        return System(*cursor.fetchone())

    def delete_economic_calc(self, system_name: str) -> EconomicCalc:
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM EconomicCalc WHERE name = ?", (system_name,))
        self.connection.commit()
        return EconomicCalc(*cursor.fetchone())

    def update_system(self, system_name: str, attribute: str, value):
        cursor = self.connection.cursor()

        if attribute == "name" or attribute == "progress" or attribute == "description":
            cursor.execute("UPDATE System SET {} = ? WHERE name = ?".format(attribute),
                         (value, system_name))
            if attribute == "name":
                cursor.execute("UPDATE EconomicCalc SET name_system = ? WHERE name_system = ?",
                               (value, system_name))

        self.connection.commit()
        return System(*cursor.fetchone())

    def update_technology(self, technology: str, attribute: str, value):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE Technology SET {} = ? WHERE technology = ?".format(attribute),
                       (value, technology))
        self.connection.commit()

    def update_panel(self, id_panel: str, attribute: str, value):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE Panel SET {} = ? WHERE id_panel = ?".format(attribute),
                       (value, id_panel))
        self.connection.commit()

    def update_hsp(self, place: str, attribute: str, value):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE Hsp SET {} = ? WHERE place = ?".format(attribute),
                       (value, place))
        self.connection.commit()

    "---------------"
    "Otras consultas"
    "---------------"

    def find_panel(self, id_panel):
        """
        Busca los sistemas donde se usen este panel.

        :param id_panel: identificador del panel.
        :return: nombre de los sistemas.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT name FROM System WHERE id_panel = ?", (id_panel,))
        self.connection.commit()

        return [f"{i}" for i in cursor.fetchall()]

    def find_hsp(self, place):
        """
        Busca los sistemas que se hagan en esta zona.

        :param place: lugar.
        :return: nombre de los sistemas.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT name FROM System WHERE place = ?", (place,))
        self.connection.commit()

        return [f"{i}" for i in cursor.fetchall()]

    def find_technology(self, technology):
        """
        Busca los sistemas que usen esta tecnologia.

        :param technology: tecnologia que usan.
        :return: nombre de los sistemas.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT name FROM System WHERE technology = ?", (technology,))
        self.connection.commit()

        return [f"{i}" for i in cursor.fetchall()]