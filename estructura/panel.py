class Tecnologia:
    def __init__(self, material, area):
        self.material = material
        self.area = area

    def to_string(self):
        return f"material: {self.material}, area: {self.area}"


class Panel:
    def __init__(self, identificador, potencia_pico, precio, precio_kwh_sen):
        self.identificador = identificador
        self.potencia_pico = potencia_pico
        self.precio = precio
        self.precio_kwh_sen = precio_kwh_sen

    def to_string(self):
        return (f"identificador: {self.identificador},"
                f" potencia_pico: {self.potencia_pico}, "
                f"precio: {self.precio},"
                f"precio_kwh_sen: {self.precio_kwh_sen}")
