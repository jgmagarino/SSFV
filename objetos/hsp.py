"""

Hsp almacena la hora solar pico de una zona en especifico.

"""


class Hsp:
    def __init__(self, zona, valor):
        self.zona = zona
        self.valor = valor

    def to_string(self):
        return f'zona: {self.zona}, valor: {self.valor}'
