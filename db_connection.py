import sqlite3


class DBConnection:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print("Se creo una coneccion con la base de datos")
            cls._instance = super(DBConnection, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect('src/database/ssfv.db', check_same_thread=False)
        return cls._instance

    def query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

