import sqlite3
import os


class DbConnection:
    """
    Clase para gestionar la conexión a una base de datos SQLite.
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

    def execute_query_all(self, query, condition: [str] = None):
        """Ejecuta una sentencia SQL y devuelve los resultados."""
        if self.__connection is None:
            print("Primero establece la conexión a la base de datos.")
            return None

        cursor = self.__connection.cursor()
        try:
            if condition is None:
                cursor.execute(query)
                self.__connection.commit()  # Para sentencias que modifican la base de datos (INSERT, UPDATE, DELETE)
                return cursor.fetchall()  # Para SELECT devolverá los resultados
            else:
                cursor.execute(query, condition)
                self.__connection.commit()
                return cursor.fetchall()

        except sqlite3.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            cursor.close()

    def execute_query_one(self, query, array):
        """Ejecuta una sentencia SQL y devuelve el resultado."""
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
        """Ejecuta una sentencia SQL."""
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
