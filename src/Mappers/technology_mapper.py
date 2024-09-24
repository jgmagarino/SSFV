from src.database.db_connection import DbConnection
from src.modules.technology_module import Technology


def get_all_technologies() -> list[Technology]:
    """
        Devuelve todas las tecnologias de la base de datos
    """
    aux_list = list()

    query = f'SELECT * FROM technology'

    db = DbConnection()
    db.connect()
    result = db.execute_query_all(query)

    for i in range(len(result)):
        technology, sur_face = result[i]
        new_technology = Technology(technology, sur_face)
        aux_list.append(new_technology)

    return aux_list


def get_technology(material) -> Technology:
    """
        Devuelve la tecnologia con el material especificado de la base de datos
    """
    query = "SELECT * FROM technology WHERE material = ?"

    db = DbConnection()
    db.connect()
    result = db.execute_query_one(query, [material])

    material, surface = result
    tech = Technology(material, surface)
    return tech
