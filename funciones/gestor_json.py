import json
import os


def guardar(direccion: str, objeto: list):
    """
    Guarda un objeto en formato JSON en la dirección especificada.
    
    Args:
        direccion (str): La dirección donde se guardará el archivo JSON.
        objeto (dict): El objeto a guardar en el archivo JSON.
    """
    with open(direccion, 'w') as archivo:
        json.dump(objeto, archivo)

    print("Guardado con exito")


def cargar(direccion: object) -> list:
    """
    Carga un objeto desde un archivo JSON en la dirección especificada.
    
    Args:
        direccion (str): La dirección desde donde se cargará el archivo JSON.
        
    Returns:
        dict: El objeto cargado desde el archivo JSON.
    """
    if os.path.exists(direccion):
        with open(direccion, 'r') as archivo:
            return json.load(archivo)
    else:
        print(f"El archivo {direccion} no existe.")
        return None


def eliminar(direccion):
    """
    Elimina un archivo JSON en la dirección especificada.
    
    Args:
        direccion (str): La dirección del archivo JSON a eliminar.
    """
    if os.path.exists(direccion):
        os.remove(direccion)
        print(f"Archivo {direccion} eliminado.")
    else:
        print(f"El archivo {direccion} no existe.")
