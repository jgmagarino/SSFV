from objects.system import System
from objects.system_calc import SystemCalc


class EconomicCalc:
    def __init__(self, system_calc: SystemCalc | list, additional_cost: bool = True):
        """
        :param system_calc: calculos basicos que se le hacen al sistema, sus atributos son
        necesarios para el calculo economico, si ya se hizo este calculo entonces se entra
        una lista con los datos.
        :param additional_cost: inicializa por defecto en True, indica que se debe sumar
        un 30% del costo de los paneles al costo total.
        """

        if isinstance(system_calc, list):
            self.id = system_calc[0]
            self.system_name = system_calc[1]
            self.cost = system_calc[2]
            self.income = system_calc[3]
            self.recovery_period = system_calc[4]
        else:

            self.system_name = system_calc.system.name

            if additional_cost:
                self.cost = system_calc.system.panel.price * system_calc.number_of_panels * 1.3
            else:
                self.cost = system_calc.system.panel.price * system_calc.number_of_panels

            self.income = system_calc.userful_energy*365 * system_calc.system.panel.price_kwh_sen

            self.recovery_period = self.cost / self.income
