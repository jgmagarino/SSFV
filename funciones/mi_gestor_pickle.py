"""
Modulo para gestinar los archivos .pkl, utilizando listas para almacenar la
informacion.


Existe un modulo llamado pickle que sirve para gestionar los archivos .pkl
pero el objetivo de este es para simplificar el trabajo con ese modulo y
resumirlo en funciones mas lejibles y faciles de usar.
"""


import dill
import os
from pathlib import Path


def cargar_informacion_pickle(direccion):
    """
    Carga un objeto desde un archivo.pkl en la ruta especificada utilizando dill para deserializar el objeto.

    :param direccion: La ruta completa del archivo desde donde se cargará el objeto.
    :return: El objeto deserializado cargado desde el archivo.
    """
    # Verifica si el archivo existe
    ruta = Path(direccion)
    if not ruta.exists():
        raise FileNotFoundError(f"El archivo {direccion} no existe.")

    # Abre el archivo en modo lectura binaria ('rb')
    with open(ruta, 'rb') as archivo:
        objeto = dill.load(archivo)

    return objeto


def guardar_informacion_pickle(direccion, objeto):
    """
    Guarda un objeto en un archivo.pkl en la ruta especificada utilizando dill para serializar el objeto.

    :param direccion: La ruta completa donde se guardará el archivo.
    :param objeto: El objeto que se desea serializar y guardar en el archivo.
    """
    # Verifica si el directorio padre existe, si no, lo crea
    ruta = Path(direccion)
    if not ruta.parent.exists():
        ruta.parent.mkdir(parents=True)

    # Abre el archivo en modo escritura binaria ('wb')
    with open(ruta, 'wb') as archivo:
        dill.dump(objeto, archivo)


def borrar_archivo_pickle(nombre_archivo):
    """
    Borra un archivo .pkl
    :param nombre_archivo: nombre del archivo
    """
    if os.path.exists(nombre_archivo):
        os.remove(nombre_archivo)
    else:
        print(f"El archivo {nombre_archivo} no existe.")


