import re
from src.modules.panel_module import Panel
from src.database.db_connection import DbConnection


class Technology:
    """
    Clase que referencia al objeto tecnologia
    """

    def __init__(self, technology: str, surface: str):
        """
        :param technology: atributo que referencia al material de cada tecnologia
        :param surface: atributo que referencia al area de cada tecnologia
        """
        self.__technology = str(technology)
        self.__surface = surface.replace(" ", "")
        self.__visible = 1

    @property
    def technology(self):
        return self.__technology

    @technology.setter
    def technology(self, value):
        self.__technology = value

    @property
    def surface(self):
        return self.__surface

    @surface.setter
    def surface(self, value):
        self.__surface = value

    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, value):
        self.__visible = value

    def save(self) -> bool:
        """
        Guarda en la base de datos el objeto correpondiente
        :return: Retorna True si el objeto esta validado correctamente
        """
        if self.validate():
            db = DbConnection()
            db.connect()

            query = """INSERT INTO Technology (material, surface, visible) VALUES (?, ?, ?)"""

            db.execute_query(query, [self.__technology, self.__surface, self.__visible])
            return True
        else:
            return False

    def delete(self) -> bool:
        """Elimina en la base de datos el objeto correpondiente """
        db = DbConnection()
        db.connect()

        query1 = """SELECT panel_id FROM Panel WHERE cell_material = ?"""
        query2 = """SELECT name FROM System WHERE panel_id = ?"""

        panel_ids = db.execute_query_all(query1, [self.__technology])
        sys_names_list = list()

        for i in range(len(panel_ids)):
            for j in range(len(panel_ids[i])):
                names = db.execute_query_all(query2, [panel_ids[i][j]])
                sys_names_list.append(names)
                db.delete_row('System', 'panel_id', panel_ids[i][j])

        for i in range(len(sys_names_list)):
            for j in range(len(sys_names_list[i])):
                for k in range(len(sys_names_list[i][j])):
                    db.delete_row('SystemCalc', "system_name", sys_names_list[i][j][k])
                    db.delete_row('EconomicCalc', "system_name", sys_names_list[i][j][k])

        db.delete_row('Panel', 'cell_material', self.__technology)
        db.delete_row('Technology', "material", self.__technology)
        return True

    def validate(self) -> bool:
        """Valida el objeto correspondiente y de ser valido retorna True"""
        check1 = re.match(r"^\d+(\.\d+)?-\d+(\.\d+)?$", self.__surface)
        check2 = True if self.__visible == 0 or self.__visible == 1 else False
        
        if check1 and check2:
            return True
        else:
            return False

    def convert_to_number(self):
        """Convierte a numeros el dato del area de la tecnologia
            :return: retorna una tupla con los datos convertidos a numeros
            Ejemplo de retorno: '7-9' => (7,9)
        """
        numbers = self.__surface.split('-')
        num1 = float(numbers[0])
        num2 = float(numbers[1])

        if num1 < num2:
            return tuple([num1, num2])
        return tuple([num2, num1])
    
    def get_panels(self):
            """Devuelve los panels donde se utiliza este objeto en una lista de objetos tipo panel"""
            aux_list = list()
            query = f'SELECT * FROM Panel WHERE cell_material = ?'

            db = DbConnection()
            db.connect()
            result = db.execute_query_all(query, [self.__technology])

            for i in range(len(result)):
                id_panel, peak_power, cell_material, area, price, price_kwh_sen, visible = result[i]
                panel = Panel(id_panel, peak_power, cell_material, area, price, price_kwh_sen)
                panel.visible = visible
                
                aux_list.append(panel)

            return aux_list
