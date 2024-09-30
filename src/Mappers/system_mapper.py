from src.database.db_connection import DbConnection
from src.modules.system_module import System


def get_all_systems() -> list[System]:
    """
        Devuelve todos los sistemas de la base de datos
    """
    aux_list = list()

    query = f'SELECT * FROM System'

    db = DbConnection()
    db.connect()
    result = db.execute_query_all(query)

    for i in range(len(result)):
        name, id_panel, place, progress, description, to_south, visible = result[i]
        new_system = System(name, id_panel, place, progress, bool(to_south))
        new_system.description = description
        new_system.visible = visible
        aux_list.append(new_system)

    return aux_list


def get_system(name) -> System | int:
    """
    Devuelve el sistema con el nombre especificado de la base de datos y si no lo encuentra devuelve -1
    """
    query = "SELECT * FROM System WHERE name = ?"

    db = DbConnection()
    db.connect()
    if exist_system(name):
        result = db.execute_query_one(query, [name])
        name, panel_id, place, progress, description, to_south, visible = result
        system = System(name, panel_id, place, progress, bool(to_south))
        system.description = description
        system.visible = visible
        return system
    return -1


def exist_system(name: str):
    """Verifica si existe en la base de datos  el objeto sistema y de ser asi retorna True"""
    db = DbConnection()
    db.connect()

    query = """SELECT 1 FROM System WHERE name = ?"""
    result = db.execute_query_one(query, [name])

    return result == (1,)
