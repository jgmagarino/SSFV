from src.database.db_connection import DbConnection
from src.modules.systemCalc_module import SystemCalc
from src.modules.system_module import System


class EconomicCalc:
    def __init__(self, system: System, system_calc: SystemCalc):
        self.__system = system
        self.__cost = 0
        self.__income = 0
        self.__recovery_period = 0
        self.__system_calc = system_calc

    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, value):
        self.__system = value

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, value):
        self.__cost = value

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, value):
        self.__income = value

    @property
    def recovery_period(self):
        return self.__recovery_period

    @recovery_period.setter
    def recovery_period(self, value):
        self.__recovery_period = value

    def calc_cost(self):
        panel_id = self.__system.panel_id
        sys_name = self.__system_calc.system.name

        db = DbConnection()
        db.connect()

        query1 = """SELECT price FROM panel WHERE panel_id = ?"""
        query2 = """SELECT number_of_panel FROM system_calc WHERE system_name = ?"""

        price = db.execute_query_one(query1, [panel_id])[0]
        number_of_panel = db.execute_query_one(query2, [sys_name])[0]

        result = price * number_of_panel
        self.cost = result
        return result

    def calc_income(self):
        panel_id = self.__system.panel_id
        sys_name = self.__system_calc.system.name

        db = DbConnection()
        db.connect()

        query1 = """SELECT price_kwh_sen FROM panel WHERE panel_id = ?"""
        query2 = """SELECT useful_energy FROM system_calc WHERE system_name = ?"""

        price_kwh_sen = db.execute_query_one(query1, [panel_id])[0]
        useful_energy = db.execute_query_one(query2, [sys_name])[0]

        result = 365 * useful_energy * price_kwh_sen
        self.income = result
        return result

    def calc_recovery_period(self):
        result = self.calc_cost() / self.calc_income()
        self.recovery_period = result
        return result

    def save(self):
        if not self.exist():
            db = DbConnection()
            db.connect()

            query = """INSERT INTO economic_calc (system_name, cost, income, recovery_period) 
                                                        VALUES (?, ?, ?, ?)"""

            db.execute_query(query, [self.__system.name, self.__cost,
                                     self.__income, self.__recovery_period])
            return True
        else:
            return False

    def delete(self):
        if self.exist():
            db = DbConnection()
            db.connect()

            db.delete_row('economic_calc', "system_name", self.__system.name)
            return True
        else:
            return False

    def exist(self):
        db = DbConnection()
        db.connect()

        query = """SELECT 1 FROM economic_calc WHERE system_name = ?"""
        result = db.execute_query_one(query, [self.__system.name])

        return result == (1,)
