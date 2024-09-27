from src.database.db_connection import DbConnection
from src.modules.economicCalc_module import EconomicCalc
from src.modules.systemCalc_module import SystemCalc
from src.modules.system_module import System


def get_all_sys_calc() -> list[SystemCalc]:
    """
    Devuelve todos los calculos del sistema en forma de lista de diccionarios con los atributos:
    sys_name -> referencia al nombre del sistema
    useful_energy -> referencia a la energia util del sistema
    num_panels -> referencia a la cantidad de paneles del sistema
    area -> referencia al area del sistema
    peak_power -> referencia a la potencia pico del sistema
    """
    aux_list = list()
    query = f'SELECT * FROM system_calc'
    query1 = f'SELECT * FROM system WHERE name = ?'

    db = DbConnection()
    db.connect()
    result = db.execute_query_all(query)

    for i in range(len(result)):
        sys_name, useful_energy, num_panels, area, peak_power = result[i]
        data = db.execute_query_one(query1, [sys_name])
        name, id_panel, place, progress, description, to_south = data
        new_system = System(name, id_panel, place, progress, bool(to_south))
        new_system.description = description

        new_calc = SystemCalc(new_system)
        new_calc.useful_energy = useful_energy
        new_calc.number_of_panels = num_panels
        new_calc.area = area
        new_calc.peak_power = peak_power

        aux_list.append(new_calc)

    return aux_list


def get_sys_calc(sys_name: str):
    """Devuelve los calculos de acuerdo al nombre del sistema"""
    query = f'SELECT * FROM system_calc WHERE system_name = ?'
    query1 = f'SELECT * FROM system WHERE name = ?'

    db = DbConnection()
    db.connect()

    result = db.execute_query_one(query, [sys_name])
    system_name, useful_energy, number_of_panels, area, peak_power = result

    data = db.execute_query_one(query1, [system_name])
    name, id_panel, place, progress, description, to_south = data
    new_system = System(name, id_panel, place, progress, bool(to_south))
    new_system.description = description

    new_calc = SystemCalc(new_system)
    new_calc.useful_energy = useful_energy
    new_calc.number_of_panels = number_of_panels
    new_calc.area = area
    new_calc.peak_power = peak_power

    return new_calc


def get_all_sys_eco_cal() -> list[EconomicCalc]:
    """
    Devuelve todos los calculos economicos del sistema en forma de lista de diccionarios con los atributos:
    sys_name -> referencia al nombre del sistema
    cost -> referencia al costo del sistema
    income -> referencia a los ingresos del sistema
    recovery_period -> referencia al periodo simple de recuperacion de la inversion del sistema
    """
    aux_list = list()
    query = f'SELECT * FROM economic_calc'
    query1 = f'SELECT * FROM system WHERE name =?'
    query2 = f'SELECT * FROM system_calc WHERE system_name =?'

    db = DbConnection()
    db.connect()
    result = db.execute_query_all(query)

    for i in range(len(result)):
        sys_name, cost, income, recovery_period = result[i]

        data = db.execute_query_one(query1, [sys_name])
        name, id_panel, place, progress, description, to_south = data
        new_system = System(name, id_panel, place, progress, bool(to_south))

        data1 = db.execute_query_one(query2, [sys_name])
        syst_name, useful_energy, num_panels, area, peak_power = data1
        new_sys_calc = SystemCalc(new_system)
        new_sys_calc.useful_energy = useful_energy
        new_sys_calc.number_of_panels = num_panels
        new_sys_calc.area = area
        new_sys_calc.peak_power = peak_power

        new_eco_calc = EconomicCalc(new_system, new_sys_calc)
        new_eco_calc.income = income
        new_eco_calc.cost = cost
        new_eco_calc.recovery_period = recovery_period

        aux_list.append(new_eco_calc)

    return aux_list


def get_eco_calc(sys_name: str):
    """Devuelve los calculos economicos de acuerdo al nombre del sistema"""
    query = f'SELECT * FROM economic_calc WHERE system_name = ?'
    query1 = f'SELECT * FROM system WHERE name =?'
    query2 = f'SELECT * FROM system_calc WHERE system_name =?'

    db = DbConnection()
    db.connect()

    result = db.execute_query_one(query, [sys_name])
    system_name, cost, income, recovery_period = result

    data = db.execute_query_one(query1, [system_name])
    name, id_panel, place, progress, description, to_south = data
    new_system = System(name, id_panel, place, progress, bool(to_south))
    new_system.description = description

    data1 = db.execute_query_one(query2, [system_name])
    syst_name, useful_energy, num_panels, area, peak_power = data1
    new_sys_calc = SystemCalc(new_system)
    new_sys_calc.useful_energy = useful_energy
    new_sys_calc.number_of_panels = num_panels
    new_sys_calc.area = area
    new_sys_calc.peak_power = peak_power

    new_eco_calc = EconomicCalc(new_system, new_sys_calc)
    new_eco_calc.income = income
    new_eco_calc.cost = cost
    new_eco_calc.recovery_period = recovery_period

    return new_eco_calc
