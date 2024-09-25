from src.database.db_connection import DbConnection


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
        if not self.exist():
            db = DbConnection()
            db.connect()

            query = """INSERT INTO hsp (place, value) VALUES (?, ?)"""

            db.execute_query(query, [self.__place, self.__value])
            return True
        else:
            return False

    def delete(self) -> bool:
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
        db = DbConnection()
        db.connect()

        query = """SELECT 1 FROM hsp WHERE place = ?"""
        result = db.execute_query_one(query, [self.__place])

        return result == (1,)

    # todo donde se usa ?
    def validate(self) -> bool:
        """Valida si los datos numericos son correctos"""
        if isinstance(self.__value, (int, float)) and self.__value > 0:
            return True
        return False
