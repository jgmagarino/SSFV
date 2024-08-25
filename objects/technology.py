class Technology:
    def __init__(self, technology: str, surface: float):
        """
        Las distintas tecnologias necesitaran un area en especifico para generar un kWp.
        Atributos:

        :param technology: el cual define a cada tecnologia por lo tanto seria la llave primaria.
        :param surface: la superficie que necesita para generar cada kWp.
        """

        self.technology = technology
        self.surface = surface
