from src.database.db_connection import DbConnection
from src.modules.hsp_module import HSP


def get_all_hps() -> list[HSP]:
    """
        Devuelve todas las horas solares pico de la base de datos
    """
    aux_list = list()

    query = f'SELECT * FROM hsp'

    db = DbConnection()
    db.connect()
    result = db.execute_query_all(query)

    for i in range(len(result)):
        place, value = result[i]
        new_hsp = HSP(place, value)
        aux_list.append(new_hsp)

    return aux_list


def get_hsp(place: str) -> HSP:
    """
        Devuelve la hora solar pico en el lugar especificado de la base de datos
    """
    query = "SELECT * FROM hsp WHERE place = ?"

    db = DbConnection()
    db.connect()
    result = db.execute_query_one(query, [place])

    place, value = result
    hsp = HSP(place, value)
    return hsp
