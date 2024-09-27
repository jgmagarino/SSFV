from src.database.db_connection import DbConnection
from src.modules.system_module import System


class HSP:

    def __init__(self, place: str, value: float):
        self.__place = str(place)
        self.__value = value
        self.__visible = 1

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        self.__place = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, value):
        self.__visible = value

    def save(self) -> bool:
        """Guarda en la base de datos el objeto correpondiente
        :return: Retorna True si el objeto esta validado correctamente"""
        if not self.exist() and self.validate():
            db = DbConnection()
            db.connect()

            query = """INSERT INTO hsp (place, value) VALUES (?, ?)"""

            db.execute_query(query, [self.__place, self.__value])
            return True
        else:
            return False

    def delete(self) -> bool:
        """Elimina el objeto correspondiente"""
        if self.exist():
            db = DbConnection()
            db.connect()

            query = """SELECT name FROM system WHERE place = ?"""
            names = db.execute_query_all(query, [self.__place])

            for i in range(len(names)):
                for j in range(len(names[i])):
                    db.delete_row('system_calc', "system_name", names[i][j])
                    db.delete_row('economic_calc', "system_name", names[i][j])

            db.delete_row('system', "place", self.__place)
            db.delete_row('hsp', "place", self.__place)
            return True
        else:
            return False

    def exist(self):
        """Verifica si existe en la base de datos el objeto correspondiente y de ser asi retorna True"""
        db = DbConnection()
        db.connect()

        query = """SELECT 1 FROM hsp WHERE place = ?"""
        result = db.execute_query_one(query, [self.__place])

        return result == (1,)

    def validate(self) -> bool:
        """Valida si los datos numericos son correctos"""
        if isinstance(self.__value, (int, float)) and self.__value > 0:
            return True
        return False

    def get_system(self) -> list[System]:
        """Devuelve los sistemas donde se utiliza este objeto en una lista de objetos tipo sistema"""
        aux_list = list()
        query = f'SELECT * FROM system WHERE place = ?'

        db = DbConnection()
        db.connect()
        result = db.execute_query_all(query, [self.__place])

        for i in range(len(result)):
            name, id_panel, place, progress, description, to_south = result[i]
            new_system = System(name, id_panel, place, progress, bool(to_south))
            aux_list.append(new_system)

        return aux_list
