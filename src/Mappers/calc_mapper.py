from src.database.db_connection import DbConnection


def get_all_sys_calc() -> list[dict]:
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

    db = DbConnection()
    db.connect()
    result = db.execute_query_all(query)

    for i in range(len(result)):
        calc_id, sys_name, useful_energy, num_panels, area, peak_power = result[i]
        new_dict = {
            'sys_name': sys_name,
            'useful_energy': useful_energy,
            'num_panels': num_panels,
            'area': area,
            'peak_power': peak_power
        }
        aux_list.append(new_dict)

    return aux_list


def get_sys_calc(sys_name: str):
    """Devuelve los calculos de acuerdo al nombre del sistema"""
    query = f'SELECT * FROM system_calc WHERE system_name = ?'

    db = DbConnection()
    db.connect()

    result = db.execute_query_one(query, [sys_name])
    id_calc, sys_name, useful_energy, number_of_panels, area, peak_power = result

    new_dict = {
        'sys_name': sys_name,
        'useful_energy': useful_energy,
        'num_panels': number_of_panels,
        'area': area,
        'peak_power': peak_power
    }
    return new_dict


def get_all_sys_eco_cal() -> list[dict]:
    """
    Devuelve todos los calculos economicos del sistema en forma de lista de diccionarios con los atributos:
    sys_name -> referencia al nombre del sistema
    cost -> referencia al costo del sistema
    income -> referencia a los ingresos del sistema
    recovery_period -> referencia al periodo simple de recuperacion de la inversion del sistema
    """
    aux_list = list()
    query = f'SELECT * FROM economic_calc'

    db = DbConnection()
    db.connect()
    result = db.execute_query_all(query)

    for i in range(len(result)):
        calc_id, sys_name, cost, income, recovery_period = result[i]
        new_dict = {
            'sys_name': sys_name,
            'cost': cost,
            'income': income,
            'recovery_period': recovery_period
        }
        aux_list.append(new_dict)

    return aux_list


def get_eco_calc(sys_name: str):
    """Devuelve los calculos economicos de acuerdo al nombre del sistema"""
    query = f'SELECT * FROM economic_calc WHERE system_name = ?'

    db = DbConnection()
    db.connect()

    result = db.execute_query_one(query, [sys_name])
    id_calc, sys_name, cost, income, recovery_period = result

    new_dict = {
        'sys_name': sys_name,
        'cost': cost,
        'income': income,
        'recovery_period': recovery_period
    }
    return new_dict
