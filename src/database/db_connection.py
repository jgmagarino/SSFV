import sqlite3
import os


class DbConnection:
    """
    Clase para gestionar la conexión a una base de datos SQLite.
    Ejemplo de conexion: { db = DbConnection()
                           db.connect() }
    """
    def __init__(self, db_name: str = 'ssfv.db'):
        self.__db_name = os.path.join(os.path.dirname(__file__), db_name)
        self.__connection = None
        self.__cursor = None

    @property
    def cursor(self):
        return self.__cursor

    @cursor.setter
    def cursor(self, value):
        self.__cursor = value

    def connect(self):
        """Establece la conexión a la base de datos SQLite."""
        if self.__connection is None:
            try:
                self.__connection = sqlite3.connect(self.__db_name)
                self.__connection.cursor().execute("""PRAGMA foreing_keys = ON""")
            except sqlite3.Error as e:
                print(f"Error al conectar a la base de datos: {e}")

    def execute_query_all(self, query, array: [str] = None):
        """
        Ejecuta una sentencia SQL y todas las coincidencias.

        :param query: sentencia SQL a ejecutar.
        Ejemplo de como tiene que ser la query: "SELECT * FROM system" o "SELECT * FROM system WHERE name = ?".

        :param array:(Es opcional en dependencia si tiene condicion de busqueda o no)variables por la que se va a sustituir por cada '?' que tenga la query anterior.
        Ejemplo de como tiene que ser el array: [variable_1, variable_2, ...., variable_n]

        :return: retorna una lista de tuplas con las coincidencias encontradas
        Ejemplo de retorno para el caso sin condicion: [(),(), ....., ()]

        """
        if self.__connection is None:
            print("Primero establece la conexión a la base de datos.")
            return None

        cursor = self.__connection.cursor()
        try:
            if array is None:
                cursor.execute(query)
                self.__connection.commit()  # Para sentencias que modifican la base de datos (INSERT, UPDATE, DELETE)
                return cursor.fetchall()  # Para SELECT devolverá los resultados
            else:
                cursor.execute(query, array)
                self.__connection.commit()
                return cursor.fetchall()

        except sqlite3.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            cursor.close()

    def execute_query_one(self, query, array):
        """
        Ejecuta una sentencia SQL y devuelve una sola coincidencia.

        :param query: sentencia SQL a ejecutar.
        Ejemplo de como tiene que ser la query: "SELECT place FROM system WHERE name = ?".

        :param array: variables por la que se va a sustituir por cada '?' que tenga la query anterior.
        Ejemplo de como tiene que ser el array: [variable_1, variable_2, ...., variable_n]

        :return: retorna una tupla.
        Ejemplo de retorno para la query anterior: ('Cienfuegos')
        """
        if self.__connection is None:
            print("Primero establece la conexión a la base de datos.")
            return None

        cursor = self.__connection.cursor()
        try:
            cursor.execute(query, array)
            self.__connection.commit()  # Para sentencias que modifican la base de datos (INSERT, UPDATE, DELETE)
            return cursor.fetchone()  # Para SELECT devolverá el resultado
        except sqlite3.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            cursor.close()

    def execute_query(self, query, array):
        """
        Ejecuta una sentencia SQL

        :param query: sentencia SQL a ejecutar.
        Ejemplo de como tiene que ser la query: "SELECT place FROM system WHERE name = ?"

        :param array: variables por la que se va a sustituir por cada '?' que tenga la query anterior
        Ejemplo de como tiene que ser: [variable_1, variable_2, ...., variable_n]

        :return: no retorna nada
        """
        if self.__connection is None:
            print("Primero establece la conexión a la base de datos.")

        cursor = self.__connection.cursor()
        try:
            cursor.execute(query, array)
            self.__connection.commit()  # Para sentencias que modifican la base de datos (INSERT, UPDATE, DELETE)
        except sqlite3.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            cursor.close()

    def delete_row(self, table, column_id, id_value):
        """
        Elimina una fila de una tabla de la base de datos

        :param table: tabla donde se va a eliminar la fila

        :param column_id: columna de la tabla que es por la que se va a eliminar

        :param id_value: valor el cual se va a verificar si es igual a la columna de la tabla por la que se va a eliminar

        :return: no retorna nada
        """
        if self.__connection is None:
            print("Primero establece la conexión a la base de datos.")

        cursor = self.__connection.cursor()
        try:
            cursor.execute(f"DELETE FROM {table} WHERE {column_id} = ? ", [id_value])
            self.__connection.commit()  # Para sentencias que modifican la base de datos (INSERT, UPDATE, DELETE)
        except sqlite3.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            cursor.close()

    def close(self):
        """Cierra la conexión a la base de datos si está abierta."""
        if self.__connection:
            self.__connection.close()
            self.__connection = None
