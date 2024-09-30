from src.database.db_connection import DbConnection
from src.modules.hsp_module import HSP


def get_all_hps() -> list[HSP]:
    """
        Devuelve todas las horas solares pico de la base de datos
    """
    aux_list = list()

    query = f'SELECT * FROM Hsp'

    db = DbConnection()
    db.connect()
    result = db.execute_query_all(query)

    for i in range(len(result)):
        place, value, visible= result[i]
        new_hsp = HSP(place, value)
        new_hsp.visible = visible
        aux_list.append(new_hsp)

    return aux_list


def get_hsp(place: str) -> HSP | int:
    """
    Devuelve la hora solar pico en el lugar especificado de la base de datos y si no lo encuentra devuelve -1
    """
    query = "SELECT * FROM Hsp WHERE place = ?"

    db = DbConnection()
    db.connect()
    if exist_hsp(place):
        result = db.execute_query_one(query, [place])
        place, value, visible = result
        hsp = HSP(place, value)
        hsp.visible = visible
        return hsp
    return -1


def exist_hsp(place: str) -> bool:
    """Verifica si existe en la base de datos el objeto HSP y de ser asi retorna True"""
    db = DbConnection()
    db.connect()

    query = """SELECT 1 FROM Hsp WHERE place = ?"""
    result = db.execute_query_one(query, [place])

    return result == (1,)
