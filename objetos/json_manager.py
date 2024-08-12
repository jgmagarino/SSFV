import json
import os.path


def create_empty_json(file_path: str):
    """
    Crea un nuevo archivo .json y le agrega una lista vacia.

    :param file_path: direccion donde creara el nuevo archivo .json
    """

    with open(file_path, 'w') as file:
        json.dump([], file, indent=4)
    print(f"Archivo json creado exitosamente, en: {file_path}")


def add_element(file_path: str, new_element: dict):
    """
    Agrega un dict a un json.

    :param file_path: direccion del json
    :param new_element: nuevo elemento
    """

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            list_elements = json.load(file)
    else:
        print(f"No existe un archivo en {file_path}")
        print(f"Se creara un .json en {file_path}")
        list_elements = []

    list_elements.append(new_element)

    with open(file_path, 'w') as file:
        json.dump(list_elements, file, indent=4)
    print(f"Nuevo diccionario agregado al archivo json: {file_path}")


def load_elements(file_path) -> list:
    """
    Carga y devuelve los elementos (lista de diccionarios) almacenados en el archivo .json.
    """
    try:
        with open(file_path, 'r') as file:
            load = json.load(file)
            print(f"Elementos cargados desde {file_path}")
            return load
    except FileNotFoundError:
        print(f"Archivo no encontrado: {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON: {file_path}")
        return []


def get_unic_value(file_path, key, value):
    """

    Extrae un elemento de un .json en funcion de una clave que tenga un valor especificado

    :param file_path: direccion del json.
    :param key: clave
    :param value: valor especificado
    :return: elemento especificado
    """

    #  Comprension de listas
    return [i for i in load_elements(file_path) if i.get(key) == value]

