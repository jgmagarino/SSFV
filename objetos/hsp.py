"""

Hsp almacena la hora solar pico de una zona en especifico.

"""


class Hsp:
    def __init__(self, zona, valor):
        self.zona = zona
        self.valor = valor

    @classmethod
    def desde_diccionario(cls, diccionario):
        return cls(**diccionario)
