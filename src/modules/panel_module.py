from src.database.db_connection import DbConnection
from src.modules.system_module import System


class Panel:
    """Clase que referencia al objeto panel"""

    def __init__(self, panel_id: str, peak_power: float, cell_material: str, area: float, price: float,
                 price_kwh_sen: float):
        """
        :param panel_id: Referencia al id del panel
        :param peak_power: Referencia a la potencia pico del panel
        :param cell_material: Referencia al material de las celdas del panel
        :param area: Referencia al area del panel
        :param price: Referencia al precio del panel
        :param price_kwh_sen: Referencia al precio por kwh del panel
        """
        self.__panel_id = str(panel_id)
        self.__peak_power = peak_power
        self.__cell_material = str(cell_material)
        self.__area = area
        self.__price = price
        self.__price_kwh_sen = price_kwh_sen
        self.__visible = 1

    @property
    def panel_id(self):
        return self.__panel_id

    @panel_id.setter
    def panel_id(self, new_id):
        self.__panel_id = new_id

    @property
    def peak_power(self):
        return self.__peak_power

    @peak_power.setter
    def peak_power(self, new_peak_power):
        self.__peak_power = new_peak_power

    @property
    def cell_material(self):
        return self.__cell_material

    @cell_material.setter
    def cell_material(self, new_cell_material):
        self.__cell_material = new_cell_material

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, new_area):
        self.__area = new_area

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price

    @property
    def price_kwh_sen(self):
        return self.__price_kwh_sen

    @price_kwh_sen.setter
    def price_kwh_sen(self, new_price_kwh_sen):
        self.__price_kwh_sen = new_price_kwh_sen

    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, new_visible):
        self.__visible = new_visible

    def save(self) -> bool:
        """Guarda en la base de datos el objeto correpondiente
        :return: Retorna True si el objeto esta validado correctamente"""
        if self.validate():
            db = DbConnection()
            db.connect()

            query = """INSERT INTO Panel (panel_id, peak_power, cell_material, area, price, price_kwh_sen, visible) 
                                                        VALUES (?, ?, ?, ?, ?, ?, ?)"""

            db.execute_query(query, [self.__panel_id, self.__peak_power, self.__cell_material, self.__area,
                                     self.__price, self.__price_kwh_sen, self.__visible])
            return True
        else:
            return False

    def delete(self) -> bool:
        """Elimina el objeto correspondiente"""
        db = DbConnection()
        db.connect()

        query = """SELECT name FROM System WHERE panel_id = ?"""
        sys_names = db.execute_query_all(query, [self.__panel_id])

        for i in range(len(sys_names)):
            for j in range(len(sys_names[i])):
                db.delete_row('SystemCalc', "system_name", sys_names[i][j])
                db.delete_row('EconomicCalc', "system_name", sys_names[i][j])

        db.delete_row('System', "place", self.__panel_id)
        db.delete_row('Panel', "panel_id", self.__panel_id)
        return True

    def validate(self) -> bool:
        """Valida si los datos numericos son correctos"""
        ch1 = isinstance(self.__peak_power, (int, float)) and self.__peak_power > 0
        ch2 = isinstance(self.__price, (int, float)) and self.__price > 0
        ch3 = isinstance(self.__area, (int, float)) and self.__area > 0
        ch4 = isinstance(self.__price_kwh_sen, (int, float)) and self.__price_kwh_sen > 0
        ch5 = True if self.__visible == 0 or self.__visible == 1 else False

        return ch1 and ch2 and ch3 and ch4 and ch5

    def get_system(self) -> list[System]:
        """Devuelve los sistemas donde se utiliza este objeto en una lista de objetos tipo sistema"""
        aux_list = list()
        query = f'SELECT * FROM System WHERE panel_id = ?'

        db = DbConnection()
        db.connect()
        result = db.execute_query_all(query, [self.__panel_id])

        for i in range(len(result)):
            name, id_panel, place, progress, description, to_south, visible = result[i]
            new_system = System(name, id_panel, place, progress, bool(to_south))
            new_system.description = description
            new_system.visible = visible
            aux_list.append(new_system)

        return aux_list
