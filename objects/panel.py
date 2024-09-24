class Panel:
    def __init__(self, id_panel: str, peak_power: float, cell_material: str,
                 area: float, price: float, price_kwh_sen: float, visible: int = 1):
        """
        Cada sistema estara compuesto por paneles.

        :param id_panel: identificador unico de cada panel
        :param peak_power: potencia pico que genera el panel
        :param cell_material: material de las celdas, referencua a la tecnologia
        :param area: area que ocupa el panel
        :param price: precio del panel (Se debe definir si es en dolares o moneda nacional)
        :param price_kwh_sen: precio del kwh sen
        :param visible: indica si esta en la papelera de reciclage (0) o no (1)
        """

        self.id_panel = id_panel
        self.peak_power = float(peak_power)
        self.cell_material = cell_material
        self.area = float(area)
        self.price = float(price)
        self.price_kwh_sen = float(price_kwh_sen)
        self.visible = visible


