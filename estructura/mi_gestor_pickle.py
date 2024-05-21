"""
Modulo para gestinar los archivos .pkl, utilizando listas para almacenar la
informacion.


Existe un modulo llamado pickle que sirve para gestionar los archivos .pkl
pero el objetivo de este es para simplificar el trabajo con ese modulo y
resumirlo en funciones mas lejibles y faciles de usar.
"""


import pickle
import os


def crear_archivo_pickle(nombre_archivo):
    """
    Crea un archivo .pkl
    :param nombre_archivo: nombre del archivo
    """
    with open(nombre_archivo, 'wb') as archivo:
        pickle.dump({}, archivo)


def cargar_informacion_pickle(nombre_archivo) -> list:
    """
    Carga un archivo .pkl
    :param nombre_archivo: nombre del archivo
    :return: retornara una lista
    """
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'rb') as archivo:
            data = pickle.load(archivo)
        return data
    else:
        print(f"El archivo {nombre_archivo} no existe.")


def guardar_informacion_pickle(nombre_archivo, data: list):
    """
    Guarda una lista en archivo .pkl
    :param nombre_archivo: nombre del archivo
    :param data: lista que se desea guardar
    """
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'wb') as archivo:
            pickle.dump(data, archivo)
    else:
        crear_archivo_pickle(nombre_archivo)
        with open(nombre_archivo, 'wb') as archivo:
            pickle.dump(data, archivo)



def borrar_archivo_pickle(nombre_archivo):
    """
    Borra un archivo .pkl
    :param nombre_archivo: nombre del archivo
    """
    if os.path.exists(nombre_archivo):
        os.remove(nombre_archivo)
    else:
        print(f"El archivo {nombre_archivo} no existe.")


