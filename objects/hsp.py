import db_connection


class Hsp:
    def __init__(self, place: str, value: float, visible: int=1):
        """
        Cada sona tiene una hora solar pico(Hsp), esto se debe tener en cuenta a la hora de crear los sistemas

        :param place: lugar donde se tiene registrado una hora solar pico, este actua como llave primaria
        :param value: valor de esa hora solar pico
        :param visible: indica si esta en la papelera de reciclage (0) o no (1)
        """

        self.place = place
        self.value = value
        self.visible = visible


    def insert(self):
        pass
