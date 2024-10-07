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
        technology, sur_face, visible = result[i]
        new_technology = Technology(technology, sur_face)
        new_technology.visible = visible
        aux_list.append(new_technology)

    return aux_list


def get_technology(material) -> Technology | int:
    """
        Devuelve la tecnologia con el material especificado de la base de datos
    """
    query = "SELECT * FROM technology WHERE material = ?"

    db = DbConnection()
    db.connect()
    if exist_techno(material):
        result = db.execute_query_one(query, [material])
        material, surface, visible = result
        tech = Technology(material, surface)
        tech.visible = visible
        return tech
    return -1


def exist_techno(material: str):
    """Verifica si existe en la base de datos  el objeto tecnologia y de ser asi retorna True"""
    db = DbConnection()
    db.connect()

    query = """SELECT 1 FROM Technology WHERE material = ?"""
    result = db.execute_query_one(query, [material])

    return result == (1,)
