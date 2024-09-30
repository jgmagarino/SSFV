from src.database.db_connection import DbConnection
from src.modules.panel_module import Panel


def get_all_panels() -> list[Panel]:
    """
    Devuelve todos los paneles de la base de datos
    """
    aux_list = list()
    query = f'SELECT * FROM Panel'

    db = DbConnection()
    db.connect()
    result = db.execute_query_all(query)

    for i in range(len(result)):
        id_panel, peak_power, cell_material, area, price, price_kwh_sen, visible = result[i]
        new_panel = Panel(id_panel, peak_power, cell_material, area, price, price_kwh_sen)
        new_panel.visible = visible
        aux_list.append(new_panel)

    return aux_list


def get_panel(panel_id: str):
    """
    Devuelve el panel con el id especificado de la base de datos y si no lo encuentra devuelve -1
    """
    query = "SELECT * FROM Panel WHERE panel_id = ?"

    db = DbConnection()
    db.connect()
    if exist_panel(panel_id):
        result = db.execute_query_one(query, [panel_id])
        id_panel, peak_power, cell_material, area, price, price_kwh_sen, visible = result
        panel = Panel(id_panel, peak_power, cell_material, area, price, price_kwh_sen)
        panel.visible = visible
        return panel
    return -1


def exist_panel(panel_id: str) -> bool:
    """Verifica si existe en la base de datos el objeto panel y de ser asi retorna True"""
    db = DbConnection()
    db.connect()

    query = """SELECT 1 FROM Panel WHERE panel_id = ?"""
    result = db.execute_query_one(query, [panel_id])

    return result == (1,)
