class Tecnologia:
    def __init__(self, material, area):
        self.material = material
        self.area = area


class Panel:
    def __init__(self, identificador, potencia_pico, precio, precio_kwh_sen):
        self.identificador = identificador
        self.potencia_pico = potencia_pico
        self.precio = precio
        self.precio_kwh_sen = precio_kwh_sen

