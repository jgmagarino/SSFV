"""
Cada sistema estara compuesto principalmente por paneles
Atributos:

id_panel: identificador unico de cada panel
peak_power: potencia pico que genera el panel
cell_material: material de las celdas
area: area que ocupa el panel
price: precio del panel (Se debe definir si es en dolares o moneda nacional)
price_kwh_sen: precio del kwh sen
"""
import os
import json


def create_panel(id_panel: str, peak_power: float, cell_material: str,
                 area: float, price: float, price_kwh_sen: float):
    """

    Crea un nuevo panel y lo almacena automaticamente en '../save/Panels.json'.

    :param id_panel: identificador unico de cada panel
    :param peak_power: potencia pico que genera el panel
    :param cell_material: material de las celdas
    :param area: area que ocupa el panel
    :param price: precio del panel (Se debe definir si es en dolares o moneda nacional)
    :param price_kwh_sen: precio del kwh sen
    """

    new_panel = {"id_panel": id_panel, "peak_power": peak_power, "cell_material": cell_material,
                 "area": area, "price": price, "price_kwh_sen": price_kwh_sen}

    if os.path.exists("../save/Panels.json"):
        with open("../save/Panels.json", 'r') as file:
            list_technology = json.load(file)
    else:
        print(f"No existe un archivo en '../save/Panels.json'")
        print(f"Se creara un .json en '../save/Panels.json'")
        list_technology = []

    list_technology.append(new_panel)

    with open("../save/Panels.json", 'w') as file:
        json.dump(list_technology, file, indent=4)
    print(f"Nuevo panel agregado al archivo json: '../save/Panels.json'")


def get_all_panels() -> list[dict]:
    """
    :return: extrae todos los paneles existentes '../save/Panels.json'.
    """

    try:
        with open("../save/Panels.json", 'r') as file:
            load = json.load(file)
            print(f"Elementos cargados desde '../save/Panels.json'")
            return load
    except FileNotFoundError:
        print(f"Archivo no encontrado: '../save/Panels.json'")
        return []
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON: '../save/Panels.json'")
        return []


def get_panel(id_panel: str) -> dict:
    """
    :param: id_panel: id del panel que se quiere extraer
    :return: Extrae el panel expecificado de '../save/Panels.json'
    """

    all_panels = get_all_panels()

    if all_panels:
        return [i for i in all_panels if i["id_panel"] == id_panel][0]


def delete_panel(id_panel: str) -> bool:
    """
    Carga todos los paneles desde '../save/Panels.json' para eliminar
    el especificado y luego las vuelve a guardar.

    :param id_panel: id del panel que se quiere eliminar
    :return: True en caso de que se elimine con exito, si no False
    """

    all_panels = get_all_panels()

    for i in all_panels:
        if i["id_panel"] == id_panel:
            all_panels.remove(i)

            with open("../save/Panels.json", 'w') as file:
                json.dump(all_panels, file, indent=4)

            return True

    print(f"No se encontro el panel {id_panel}")
    return False


def clear_panels():
    """
    Elimina todos los paneles
    """

    with open("../save/Panels.json", 'w') as file:
        json.dump([], file, indent=4)


def update_panel(id_panel: str, peak_power: float=None, cell_material: str=None,
                 area: float=None, price: float=None, price_kwh_sen: float=None) -> bool:

    all_panels = get_all_panels()

    for i in all_panels:
        if i["id_panel"] == id_panel:
            if peak_power is not None:
                i["peak_power"] = peak_power
            if cell_material is not None:
                i["cell_material"] = cell_material
            if area is not None:
                i["area"] = area
            if price is not None:
                i["price"] = price
            if price_kwh_sen is not None:
                i["price_kwh_sen"] = price_kwh_sen

            with open("../save/Panels.json", 'w') as file:
                json.dump(all_panels, file, indent=4)

            return True

    print(f"No se encontro el panel {id_panel}")
    return False

