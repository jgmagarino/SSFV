import re


class InvalidDomain(Exception):
    pass


class Technology:
    def __init__(self, technology: str, surface: str, visible: int=1):
        """
        Las distintas tecnologias necesitaran un area en especifico para generar un kWp.
        Atributos:

        :param technology: el cual define a cada tecnologia por lo tanto seria la llave primaria.
        :param surface: la superficie que necesita para generar cada kWp.
        """

        # Exprecion regular para un rango de numeros con coma, ejemplo 7-9.5
        patron = r'^\d+(\.\d+)?[ ]*-[ ]*\d+(\.\d+)?$'

        if re.match(patron, surface):
            a, b = map(float, surface.split('-'))
            self.surface = (a, b) if a <= b else (b, a)
            self.technology = technology
        else:
            raise InvalidDomain(f"La cadena {surface} no es valida como rango de la superficie necesaria")

        self.visible = visible

    def get_surface_str(self):
        return f'{self.surface[0]}-{self.surface[1]}'
