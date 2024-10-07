from src.database.db_connection import DbConnection


class System:
    """Clase que referencia al sistema"""
    def __init__(self, name: str, panel_id: str, place: str, progress: int = 1,
                 to_south: bool = False, description: str = 'no hay descripcion'):
        """
        :param name: Referencia al nombre del sistema
        :param panel_id: Referencia al id del panel utilizado en el sistema
        :param place: Referencia al lugar de la hora solar pico utilizada por el sistema
        :param progress: Referencia al progreso del sistema
        :param to_south: Referencia a si es sistema anterior esta en posicion al sur o no
        """
        self.__to_south = to_south
        self.__name = str(name)
        self.__panel_id = str(panel_id)
        self.__place = str(place)
        self.__description = description
        self.__progress = progress
        self.__visible = 1

    @property
    def to_south(self):
        return self.__to_south

    @to_south.setter
    def to_south(self, value):
        self.__to_south = value

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
        """Guarda en la base de datos el objeto correpondiente
        :return: Retorna True si el objeto esta validado correctamente"""
        if self.validate():
            db = DbConnection()
            db.connect()

            query = """INSERT INTO System (name, panel_id, place, progress, description, to_south, visible) 
                                                        VALUES (?, ?, ?, ?, ?, ?, ?)"""

            db.execute_query(query, [self.__name, self.__panel_id, self.__place,
                                self.__progress, self.__description, str(self.__to_south), self.__visible])
            return True
        return False

    def delete(self) -> bool:
        """Elimina en la base de datos el objeto correpondiente """
        db = DbConnection()
        db.connect()

        db.delete_row('SystemCalc', "system_name", self.__name)
        db.delete_row('EconomicCalc', "system_name", self.__name)
        db.delete_row('System', "name", self.__name)
        return True
    
    def validate(self) -> bool:
        ch1 = True if self.__visible == 0 or self.__visible == 1 else False
        return ch1
    