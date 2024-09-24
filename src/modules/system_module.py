from src.database.db_connection import DbConnection


class System:

    def __init__(self, name: str, panel_id: str, place: str, progress: int = 1):
        self.__name = str(name)
        self.__panel_id = str(panel_id)
        self.__place = str(place)
        self.__description = 'no hay descripcion'
        self.__progress = progress
        self.__visible = 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def panel_id(self):
        return self.__panel_id

    @panel_id.setter
    def panel_id(self, value):
        self.__panel_id = value

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        self.__place = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def progress(self):
        return self.__progress

    @progress.setter
    def progress(self, value):
        self.__progress = value

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

            query = """INSERT INTO system (name, panel_id, place, progress, description) 
                                                        VALUES (?, ?, ?, ?, ?)"""

            db.execute_query(query, [self.__name, self.__panel_id, self.__place, self.__progress, self.__description])
            return True
        else:
            return False

    def delete(self) -> bool:
        if self.exist():
            db = DbConnection()
            db.connect()

            db.delete_row('system_calc', "system_name", self.__name)
            db.delete_row('economic_calc', "system_name", self.__name)
            db.delete_row('system', "name", self.__name)
            return True
        else:
            return False

    def exist(self):
        db = DbConnection()
        db.connect()

        query = """SELECT 1 FROM system WHERE name = ?"""
        result = db.execute_query_one(query, [self.__name])

        return result == (1,)
