from objects.system import System


class SystemCalc:

    def __init__(self, system: System, to_south: bool = False):
        self.system = system
        self.to_south = to_south

        self.userful_energy = 0.0
        self.number_of_panels = 0
        self.area = 0.0
        self.peak_power = 0.0


class SystemCalcPeakPower(SystemCalc):
    def __init__(self, system: System, surface_available: float, to_south: bool = False):
        """
        En caso de que se disponga de un area en especifico, se deben hacer los calculos
        del sistema con respecto a esta.

        :param system: sistema
        :param surface_available: area disponible
        :param to_south: si estan los paneles orientados al sur
        """
        super().__init__(system, to_south)

        self.area = surface_available

        self.approx_peak_power = self.area / self.system.technology.surface[0]

        if self.to_south:
            self.number_of_panels = self.area / (self.system.panel.area * 1.4)
        else:
            self.number_of_panels = self.area / self.system.panel.area

        if self.to_south:
            self.peak_power = (self.number_of_panels * self.system.panel.peak_power)*0.8
        else:
            self.peak_power = self.number_of_panels * self.system.panel.peak_power

        self.userful_energy = self.peak_power * self.system.hsp.value


class SystemCalcArea(SystemCalc):
    def __init__(self, system: System, peak_power: float, to_south: bool = False):
        """
        En caso de que se tenga una potencia a instalar, se deben hacer los calculos
        del sistema con respecto a esta.

        :param system: sistema
        :param peak_power: potencia a isntalar
        :param to_south: si estan los paneles orientados al sur
        """
        super().__init__(system, to_south)

        self.peak_power = peak_power

        self.approx_surface_required = self.peak_power * self.system.technology.surface[0]

        self.userful_energy = self.peak_power * self.system.hsp.value

        self.number_of_panels = (self.userful_energy / 0.654 * self.system.hsp.value
                                * self.system.panel.peak_power) + 1

        if self.to_south:
            self.area = self.number_of_panels * self.system.panel.area * 1.4
            self.peak_power *= 0.8
        else:
            self.area = self.number_of_panels * self.system.panel.area





