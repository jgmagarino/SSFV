"""
Las distinats tecnologias necesitaran un area en especifico para generar un kWp.
Atributos:

technology: el cual define a cada tecnologia por lo tanto seria la llave primaria.
surface: la superficie que necesita para generar cada kWp.
"""
import os
import json


def create_technology(technology: str, surface: float):
    """

    Crea una nueva tecnologia y la almacena automaticamente en '../save/Technologies.json'.

    :param technology: el cual define a cada tecnologia por lo tanto seria la llave primaria.
    :param surface: la superficie que necesita para generar cada kWp.
    """

    new_technology = {"technology": technology, "surface": surface}

    if os.path.exists("../save/Technologies.json"):
        with open("../save/Technologies.json", 'r') as file:
            list_technology = json.load(file)
    else:
        print(f"No existe un archivo en '../save/Technologies.json'")
        print(f"Se creara un .json en '../save/Technologies.json'")
        list_technology = []

    list_technology.append(new_technology)

    with open("../save/Technologies.json", 'w') as file:
        json.dump(list_technology, file, indent=4)
    print(f"Nueva tecnologia agregada al archivo json: '../save/Technologies.json'")


def get_all_technologies() -> list[dict]:
    """
    :return: extrae todas las tecnologias existentes '../save/Technologies.json'.
    """

    try:
        with open("../save/Technologies.json", 'r') as file:
            load = json.load(file)
            print(f"Elementos cargados desde '../save/Technologies.json'")
            return load
    except FileNotFoundError:
        print(f"Archivo no encontrado: '../save/Technologies.json'")
        return []
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON: '../save/Technologies.json'")
        return []


def get_technology(technology: str) -> dict:
    """
    :param: technology: tecnologia que se quiere extraer
    :return: Extrae la tecnologia especificada de '../save/Technologies.json'
    """

    all_technology = get_all_technologies()

    if all_technology:
        return [i for i in all_technology if i["technology"] == technology][0]


def delete_technology(technology: str) -> bool:
    """
    Carga todas las tecnologias desde '../save/Technologies.json' para eliminar
    la especificada y luego las vuelve a guardar.

    :param technology: tecnologia que se quiere eliminar
    :return: True en caso de que se elimine con exito, si no False
    """

    all_technology = get_all_technologies()

    for i in all_technology:
        if i["technology"] == technology:
            all_technology.remove(i)

            with open("../save/Technologies.json", 'w') as file:
                json.dump(all_technology, file, indent=4)

            return True

    print(f"No se encontro la tecnologia {technology}")
    return False

def clear_technologies():
    """
    Elimina todas las tecnologias
    """

    with open("../save/Technologies.json", 'w') as file:
        json.dump([], file, indent=4)


def update_surface(technology: str, surface: float) -> bool:
    """
    Modifica la superficie que ocupa una tecnologia

    :param technology: tecnologia que se quiere modificar
    :param surface: nueva superficie
    :return: True en caso de que se modifique con exito, si no False
    """

    all_technology = get_all_technologies()

    for i in all_technology:
        if i["technology"] == technology:
            i["surface"] = surface

            with open("../save/Technologies.json", 'w') as file:
                json.dump(all_technology, file, indent=4)

            return True

    print(f"No se encontro la tecnologia: {technology}")
    return False



