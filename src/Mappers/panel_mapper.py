from src.database.db_connection import DbConnection
from src.modules.panel_module import Panel


def get_all_panels() -> list[Panel]:
    """
    Devuelve todos los paneles de la base de datos
    """
    aux_list = list()
    query = f'SELECT * FROM panel'

    db = DbConnection()
    db.connect()
    result = db.execute_query_all(query)

    for i in range(len(result)):
        id_panel, peak_power, cell_material, area, price, price_kwh_sen = result[i]
        new_panel = Panel(id_panel, peak_power, cell_material, area, price, price_kwh_sen)
        aux_list.append(new_panel)

    return aux_list


def get_panel(panel_id: str) -> Panel:
    """
        Devuelve el panel con el id especificado de la base de datos
    """
    query = "SELECT * FROM panel WHERE panel_id = ?"

    db = DbConnection()
    db.connect()
    result = db.execute_query_one(query, [panel_id])

    id_panel, peak_power, cell_material, area, price, price_kwh_sen = result
    panel = Panel(id_panel, peak_power, cell_material, area, price, price_kwh_sen)
    return panel
