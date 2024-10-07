from src.database.db_connection import DbConnection
from src.modules.system_module import System


def get_all_systems() -> list[System]:
    """
        Devuelve todos los sistemas de la base de datos
    """
    aux_list = list()

    query = f'SELECT * FROM system'

    db = DbConnection()
    db.connect()
    result = db.execute_query_all(query)

    for i in range(len(result)):
        name, id_panel, place, progress, description, to_south = result[i]
        new_system = System(name, id_panel, place, progress, bool(to_south), description)
        aux_list.append(new_system)

    return aux_list


def get_system(name) -> System:
    """
    Devuelve el sistema con el nombre especificado de la base de datos
    """
    query = "SELECT * FROM system WHERE name = ?"

    db = DbConnection()
    db.connect()
    result = db.execute_query_one(query, [name])

    name, panel_id, place, progress, description, to_south = result
    system = System(name, panel_id, place, progress, bool(to_south), description)
    return system
