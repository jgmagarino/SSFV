"""
Cada sona tiene una hora solar pico(Hsp), esto se debe tener en cuenta a la hora de crear los sistemas

Atributos:
place: lugar donde se tiene registrado una hora solar pico, este actua como llave primaria
value: valor de esa hora solar pico

"""

import os
import json


def create_hsp(place: str, value: float):
    """

    Crea un nuevo hsp y lo guarda en '../save/Hsp.json'

    :param place: lugar donde se tiene registrado una hora solar pico, este actua como llave primaria
    :param value: valor de esa hora solar pico
    """

    new_hsp = {"place": place, "value": value}

    if os.path.exists("../save/Hsp.json"):
        with open("../save/Hsp.json", 'r') as file:
            list_hsp = json.load(file)
    else:
        print(f"No existe un archivo en '../save/Hsp.json'")
        print(f"Se creara un .json en '../save/Hsp.json'")
        list_hsp = []

    list_hsp.append(new_hsp)

    with open("../save/Hsp.json", 'w') as file:
        json.dump(list_hsp, file, indent=4)
    print(f"Nueva hsp agregada al archivo json: '../save/Hsp.json'")


def get_all_hsp() -> list[dict]:
    """
    :return: extrae todas las hsp existentes '../save/Hsp.json'.
    """

    try:
        with open("../save/Hsp.json", 'r') as file:
            load = json.load(file)
            print(f"Elementos cargados desde '../save/Hsp.json'")
            return load
    except FileNotFoundError:
        print(f"Archivo no encontrado: '../save/Hsp.json'")
        return []
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON: '../save/Hsp.json'")
        return []


def get_hsp(place: str) -> dict:
    """
    :param: place: hsp que se quiere extraer
    :return: Extrae la hsp especificada de '../save/Technologies.json'
    """

    all_hsp = get_all_hsp()

    if all_hsp:
        return [i for i in all_hsp if i["place"] == place][0]


def delete_hsp(place: str) -> bool:
    """
    Carga todas las tecnologias desde '../save/Hsp.json' para eliminar
    la hsp especificada y luego las vuelve a guardar.

    :param place: hsp que se quiere eliminar
    :return: True en caso de que se elimine con exito, si no False
    """

    all_hsp = get_all_hsp()

    for i in all_hsp:
        if i["place"] == place:
            all_hsp.remove(i)

            with open("../save/Hsp.json", 'w') as file:
                json.dump(all_hsp, file, indent=4)

            return True

    print(f"No se encontro la hsp de {place}")
    return False

def clear_hsp():
    """
    Elimina todas las tecnologias
    """

    with open("../save/Hsp.json", 'w') as file:
        json.dump([], file, indent=4)


def update_surface(place: str, value: float) -> bool:
    """
    Modifica la superficie que ocupa una tecnologia

    :param place: lugar al que se le quiere modificar la hsp
    :param value: nuevo  valor de la hsp
    :return: True en caso de que se modifique con exito, si no False
    """

    all_hsp = get_all_hsp()

    for i in all_hsp:
        if i["place"] == place:
            i["value"] = value

            with open("../save/Hsp.json", 'w') as file:
                json.dump(all_hsp, file, indent=4)

            return True

    print(f"No se encontro la hsp de {place}")
    return False
