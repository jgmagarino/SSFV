import re
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

    # todo solucion provisional, hay que pensar una forma de gestionar esto mejor
    def get_min_surface_req(self):
        """
        :return: superficie minima requerida por esta recnologia para generar un kw
        """

        aux_string = ""
        for i in self.__surface:
            if i == "-" or i == " ":
                break
            else:
                aux_string += i

        return float(aux_string)


    def save(self) -> bool:
        """
        Guarda en la base de datos el objeto correpondiente
        :return: Retorna True si el objeto esta validado correctamente
        """
        if not self.exist() and self.validate():
            db = DbConnection()
            db.connect()

            query = """INSERT INTO technology (material, surface) VALUES (?, ?)"""

            db.execute_query(query, [self.__technology, self.__surface])
            return True
        else:
            return False

    def delete(self) -> bool:
        """Elimina en la base de datos el objeto correpondiente """
        if self.exist():
            db = DbConnection()
            db.connect()

            query1 = """SELECT panel_id FROM panel WHERE cell_material = ?"""
            query2 = """SELECT name FROM system WHERE panel_id = ?"""

            panel_ids = db.execute_query_all(query1, [self.__technology])
            sys_names_list = list()

            for i in range(len(panel_ids)):
                for j in range(len(panel_ids[i])):
                    names = db.execute_query_all(query2, [panel_ids[i][j]])
                    sys_names_list.append(names)
                    db.delete_row('system', 'panel_id', panel_ids[i][j])

            for i in range(len(sys_names_list)):
                for j in range(len(sys_names_list[i])):
                    for k in range(len(sys_names_list[i][j])):
                        db.delete_row('system_calc', "system_name", sys_names_list[i][j][k])
                        db.delete_row('economic_calc', "system_name", sys_names_list[i][j][k])

            db.delete_row('panel', 'cell_material', self.__technology)
            db.delete_row('technology', "material", self.__technology)
            return True
        else:
            return False

    def exist(self):
        """Verifica si existe en la base de datos  el objeto correspondiente y de ser asi retorna True"""
        db = DbConnection()
        db.connect()

        query = """SELECT 1 FROM technology WHERE material = ?"""
        result = db.execute_query_one(query, [self.__technology])

        return result == (1,)

    def validate(self) -> bool:
        """Valida el objeto correspondiente y de ser valido retorna True"""
        if re.match(r"^\d+(\.\d+)?-\d+(\.\d+)?$", self.__surface):
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

