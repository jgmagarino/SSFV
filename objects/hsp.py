class Hsp:
    def __init__(self, place: str, value: float):
        """
        Cada sona tiene una hora solar pico(Hsp), esto se debe tener en cuenta a la hora de crear los sistemas

        :param place: lugar donde se tiene registrado una hora solar pico, este actua como llave primaria
        :param value: valor de esa hora solar pico
        """

        self.place = place
        self.value = value
