import sqlite3

from db_connection import DBConnection
from objects.economic_calc import EconomicCalc
from objects.panel import Panel
from objects.hsp import Hsp
from objects.technology import Technology
from objects.system import System


"---------------------------------------------"
"Operaciones de insertar, eliminar y modificar"
"---------------------------------------------"


def insert_hsp(hsp: Hsp):
    cursor = DBConnection().connection.cursor()
    try:
        cursor.execute("INSERT INTO Hsp (place, value) VALUES (?, ?);",
                       (
                           hsp.place,
                           hsp.value)
                       )
        DBConnection().connection.commit()
    except sqlite3.IntegrityError as e:
        if "UNIQUE constraint failed" in str(e):
            return "Ya existe una hora solar pico de esa zona"
        else:
            return "Ocurrio un error en la base de datos"



def insert_panel(panel: Panel):
    cursor = DBConnection().connection.cursor()
    try:
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
        DBConnection().connection.commit()
    except sqlite3.IntegrityError as e:
        if "UNIQUE constraint failed" in str(e):
            return "Ya existe un panel con ese identificador"
        else:
            return "Ocurrio un error en la base de datos"



def insert_technology(technology: Technology):
    cursor = DBConnection().connection.cursor()
    try:
        cursor.execute("INSERT INTO Technology (technology, surface) "
                       "VALUES (?, ?);",
                       (
                           technology.technology,
                           technology.get_surface_str())
                       )
        DBConnection().connection.commit()
    except sqlite3.IntegrityError as e:
        if "UNIQUE constraint failed" in str(e):
            return "Ya existe una tecnologia con ese identificador"
        else:
            return "Ocurrio un error en la base de datos"



def insert_economic_calc(economic_calc: EconomicCalc):
    cursor = DBConnection().connection.cursor()

    try:
        cursor.execute("INSERT INTO EconomicCalc (name_system, cost, income, recovery_period)"
                       "VALUES (?, ?, ?, ?);",
                       (
                           economic_calc.system_name,
                           economic_calc.cost,
                           economic_calc.income,
                           economic_calc.recovery_period
                       )
                       )
        DBConnection().connection.commit()
    except sqlite3.IntegrityError as e:
        if "UNIQUE constraint failed" in str(e):
            return "Ya existe un calculo economico de ese sistema"
        else:
            return "Ocurrio un error en la base de datos"



def insert_system(system: System, economic_calc: EconomicCalc = None):
    cursor = DBConnection().connection.cursor()
    try:
        cursor.execute("INSERT INTO System (name, progress, description, id_panel, place)"
                       "VALUES (?, ?, ?, ?, ?);",
                       (
                           system.name,
                           system.progress,
                           system.description,
                           system.panel.id_panel,
                           system.hsp.place,
                       )
                       )

        if economic_calc is not None: insert_economic_calc(economic_calc)

        DBConnection().connection.commit()
    except sqlite3.IntegrityError as e:
        if "UNIQUE constraint failed" in str(e):
            return "Ya existe un sistema con ese nombre"
        else:
            return "Ocurrio un error en la base de datos"


def get_all_panels() -> list[Panel]:
    cursor = DBConnection().connection.cursor()
    cursor.execute("SELECT * FROM Panel")

    panels = [Panel(*i) for i in cursor.fetchall()]

    return panels


def get_all_hsp() -> list[Hsp]:
    cursor = DBConnection().connection.cursor()
    cursor.execute("SELECT * FROM Hsp")

    hsp = [Hsp(*i) for i in cursor.fetchall()]

    return hsp


def get_all_technologies() -> list[Technology]:
    cursor = DBConnection().connection.cursor()
    cursor.execute("SELECT * FROM Technology")

    technologies = [Technology(*i) for i in cursor.fetchall()]

    return technologies


def get_all_systems() -> list[System]:
    cursor = DBConnection().connection.cursor()
    cursor.execute("SELECT * FROM System")

    systems = [System(*i) for i in cursor.fetchall()]

    return systems


def get_all_economic_calcs() -> list[EconomicCalc]:
    cursor = DBConnection().connection.cursor()
    cursor.execute("SELECT * FROM EconomicCalc")

    economic_calcs = [EconomicCalc(*i) for i in cursor.fetchall()]

    return economic_calcs


def get_panel(id_panel: str) -> Panel:
    cursor = DBConnection().connection.cursor()
    cursor.execute("SELECT * FROM Panel WHERE id_panel = ?",
                   (id_panel,))

    return Panel(*cursor.fetchone())


def get_hsp(place: str) -> Hsp:
    cursor = DBConnection().connection.cursor()
    cursor.execute("SELECT * FROM Hsp WHERE place = ?",
                   (place,))

    return Hsp(*cursor.fetchone())


def get_technology(technology: str) -> Technology:
    cursor = DBConnection().connection.cursor()
    cursor.execute("SELECT * FROM Technology WHERE technology = ?",
                   (technology,))

    return Technology(*cursor.fetchone())


def get_system(name: str) -> System:
    cursor = DBConnection().connection.cursor()
    cursor.execute("SELECT * FROM System WHERE name = ?", (name,))

    return System(*cursor.fetchone())


def get_economic_calc(system_name: str) -> EconomicCalc:
    cursor = DBConnection().connection.cursor()
    cursor.execute("SELECT * FROM EconomicCalc WHERE name_system = ?", (system_name,))

    return EconomicCalc(*cursor.fetchone())


def delete_all_panels():
    cursor = DBConnection().connection.cursor()
    cursor.execute("DELETE FROM Panel")
    DBConnection().connection.commit()


def delete_all_hsp():
    cursor = DBConnection().connection.cursor()
    cursor.execute("DELETE FROM Hsp")
    DBConnection().connection.commit()


def delete_all_technologies():
    cursor = DBConnection().connection.cursor()
    cursor.execute("DELETE FROM Technology")
    DBConnection().connection.commit()


def delete_all_systems():
    cursor = DBConnection().connection.cursor()
    cursor.execute("DELETE FROM System")
    DBConnection().connection.commit()


def delete_all_economic_calcs():
    cursor = DBConnection().connection.cursor()
    cursor.execute("DELETE FROM EconomicCalc")
    DBConnection().connection.commit()


def delete_panel(id_panel: str):
    cursor = DBConnection().connection.cursor()
    cursor.execute("DELETE FROM Panel WHERE id_panel = ?", (id_panel,))
    DBConnection().connection.commit()


def delete_hsp(place: str):
    cursor = DBConnection().connection.cursor()
    cursor.execute("DELETE FROM Hsp WHERE place = ?", (place,))
    DBConnection().connection.commit()


def delete_technology(technology: str):
    cursor = DBConnection().connection.cursor()
    cursor.execute("DELETE FROM Technology WHERE technology = ?", (technology,))
    DBConnection().connection.commit()


def delete_system(system_name: str):
    cursor = DBConnection().connection.cursor()
    cursor.execute("DELETE FROM System WHERE name = ?", (system_name,))
    DBConnection().delete_economic_calc(system_name)
    DBConnection().connection.commit()


def delete_economic_calc(self, system_name: str):
    cursor = DBConnection().connection.cursor()
    cursor.execute("DELETE FROM EconomicCalc WHERE name_system = ?", (system_name,))
    DBConnection().connection.commit()


def update_system(system_name: str, attribute: str, value):
    cursor = DBConnection().connection.cursor()

    if attribute == "name" or attribute == "progress" or attribute == "description":
        cursor.execute("UPDATE System SET {} = ? WHERE name = ?".format(attribute),
                       (value, system_name))
        if attribute == "name":
            cursor.execute("UPDATE EconomicCalc SET name_system = ? WHERE name_system = ?",
                           (value, system_name))

    DBConnection().connection.commit()
    return System(*cursor.fetchone())


def update_technology(technology: str, attribute: str, value):
    cursor = DBConnection().connection.cursor()
    cursor.execute("UPDATE Technology SET {} = ? WHERE technology = ?".format(attribute),
                   (value, technology))
    DBConnection().connection.commit()


def update_panel(id_panel: str, attribute: str, value):
    cursor = DBConnection().connection.cursor()
    cursor.execute("UPDATE Panel SET {} = ? WHERE id_panel = ?".format(attribute),
                   (value, id_panel))
    DBConnection().connection.commit()


def update_hsp(place: str, attribute: str, value):
    cursor = DBConnection().connection.cursor()
    cursor.execute("UPDATE Hsp SET {} = ? WHERE place = ?".format(attribute),
                   (value, place))
    DBConnection().connection.commit()


"---------------"
"Otras consultas"
"---------------"


def find_panel(id_panel):
    """
    Busca los sistemas donde se usen este panel.

    :param id_panel: identificador del panel.
    :return: nombre de los sistemas.
    """
    cursor = DBConnection().connection.cursor()
    cursor.execute("SELECT name FROM System WHERE id_panel = ?", (id_panel,))
    DBConnection().connection.commit()

    return [f"{i}" for i in cursor.fetchall()]


def find_hsp(place):
    """
    Busca los sistemas que se hagan en esta zona.

    :param place: lugar.
    :return: nombre de los sistemas.
    """
    cursor = DBConnection().connection.cursor()
    cursor.execute("SELECT name FROM System WHERE place = ?", (place,))
    DBConnection().connection.commit()

    return [f"{i}" for i in cursor.fetchall()]


def used_panels(not_used: bool = False):
    if not_used:
        all_panels = get_all_panels()
        used_panels = [i.panel for i in get_all_systems()]

        return [i for i in all_panels if i not in used_panels]
    else:
        return [i.panel for i in get_all_systems()]


def used_hsp(not_used: bool = False):
    if not_used:
        all_hsp = get_all_hsp()
        used_hsp = [i.hsp for i in get_all_systems()]

        return [i for i in all_hsp if i not in used_hsp]
    else:
        return [i.hsp for i in get_all_systems()]


def used_technologies(not_used: bool = False):
    if not_used:
        all_technologies = get_all_technologies()
        used_technologies = [i.hsp for i in get_all_systems()]

        return [i for i in all_technologies if i not in used_technologies]
    else:
        return [i.technology for i in get_all_systems()]

