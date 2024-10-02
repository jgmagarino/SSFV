import flet as ft

from src.Mappers.technology_mapper import get_technology
from src.modules.economicCalc_module import EconomicCalc
from src.modules.hsp_module import HSP
from src.modules.panel_module import Panel
from components.calc_descriptions_text import *
from src.modules.systemCalc_module import SystemCalc
from src.modules.system_module import System
from style import text_filed, error_text


class InvalidParams(Exception):
    """
    SI en un constructor se pasan los parametros de forma incorrecta.
    """
    pass


class Calc(ft.Container):

    def __init__(self, hsp: HSP, panel: Panel, to_south: bool,
                 area: float=None, peak_power_required: float=None):
        """
        En esta clase se realizan todos los calculos del sistema, para mostrarlos luego
        y comprobar si se debe realizar el sistema o no.

        :param hsp: hora solar pico.
        :param panel: panel que se usara
        :param to_south: estan horientados al sur (True) o no (False)
        :param area: area disponible para la construccion del sistema
        :param peak_power_required: potencia pico que se requiere en el sistema
        """
        super().__init__()

        if ((area is None and peak_power_required is None) or
                (area is not None and peak_power_required is not None)):
            raise InvalidParams("Error: Solo se puede trabajar con un area especifca o "
                                "con una potencia requerida")

        self.panel = panel
        self.hsp = hsp.value
        self.hsp_place = hsp.place
        self.to_south = to_south

        system_calc_descriptions = [ft.Text("Calculos del sistema:", size=20, color=ft.colors.BLUE)]
        economic_calc_buttons = [ft.Text("Calculos economicos:", size=20, color=ft.colors.BLUE)]

        def data_description(data: str, description: str):
            """
            sirve para agrupar el resultado de un calculo en especifico y que al tocar en el boton
            muestre los detalles de como se llego a ese resultado.

            :param data: dato o resultado del calculo
            :param description: descrupcion de los calculos
            :return: container con el boton y toda la informacion
            """
            def show(e):
                details.visible = not details.visible
                self.update()

            details = ft.Text(description, visible=False)
            button = ft.ElevatedButton(text=data, on_click=show)

            return ft.Container(
                ft.Column([
                    button,
                    details
                ]),
                border=ft.border.all(1, ft.colors.BLUE),
                padding=10,
                border_radius=10,
                width=300
            )

        "-------------------"
        "Calculo del sistema"
        "-------------------"

        # superficie requerida por la tecnologia del panel
        surface_required = get_technology(panel.cell_material).convert_to_number()[1]

        if area is not None:

            self.area = area

            # potencia pico aproximada
            self.approx_peak_power = round(self.area / surface_required, 2)
            system_calc_descriptions.append(
                data_description(f"potencia pico aproximada: {self.approx_peak_power} W",
                                 clac_approx_peak_power(self.area, surface_required))
            )

            # numero de paneles
            self.number_of_panels = int((self.area / panel.area)/ 1.4) if to_south \
                else int(self.area / panel.area)

            system_calc_descriptions.append(
                data_description(f"numero de paneles: {self.number_of_panels}",
                    calc_number_of_panels_with_area(self.area, panel.area, to_south))
            )

            if to_south:
                # potencia pico
                self.peak_power_system = self.number_of_panels * panel.peak_power
            else:
                # potencia pico
                self.peak_power_system = self.number_of_panels * panel.peak_power
                self.peak_power_system *= 0.8

            self.peak_power_system = round(self.peak_power_system, 2)

            system_calc_descriptions.append(
                data_description(f"potencia pico: {self.peak_power_system} W",
                    calc_peak_power_with_area(self.number_of_panels, panel.peak_power, to_south))
            )

            # energia util
            self.userful_energy = self.peak_power_system * self.hsp

            system_calc_descriptions.append(
                data_description(f"energia util: {self.userful_energy} Wh/día",
                    calc_userful_energy(self.peak_power_system, self.hsp))
            )

        elif peak_power_required is not None:

            self.peak_power_system = peak_power_required

            self.approx_area_required = round((self.peak_power_system/1000) * surface_required, 2)

            system_calc_descriptions.append(
                data_description(f"area aproximada: {self.approx_area_required} m^2",
                    calc_approx_area_required(self.peak_power_system, surface_required))
            )

            self.userful_energy = round(self.peak_power_system * self.hsp, 2)

            system_calc_descriptions.append(
                data_description(f"energia util: {self.userful_energy} Wh/día",
                                 calc_userful_energy(self.peak_power_system, self.hsp))
            )

            self.number_of_panels = int((self.userful_energy / (0.654 * self.hsp * panel.peak_power)) + 1 )

            system_calc_descriptions.append(
                data_description(f"numero de paneles: {self.number_of_panels}",
                    calc_number_of_panels_with_peak_power(self.userful_energy, self.hsp, panel.peak_power))
            )

            self.area = round(self.number_of_panels * panel.area, 2)

            system_calc_descriptions.append(
                data_description(f"area: {self.area} m^2",
                    calc_area_with_peak_power(self.number_of_panels, panel.area, to_south))
            )

            if to_south:
                self.area *= 1.4
            else:
                self.peak_power_system *= 0.8

        "-------------------"
        "Calculo economico"
        "-------------------"

        self.cost = round(panel.price * self.number_of_panels * 1.3, 2)

        economic_calc_buttons.append(
            data_description(f"costo del sistema: {self.cost} cup",
                             calc_cost(panel.price, self.number_of_panels))
        )

        self.income = round((self.userful_energy/1000) * 365 * panel.price_kwh_sen, 2)

        economic_calc_buttons.append(
            data_description(f"ingresos por año: {self.income} cup",
                             calc_income(self.userful_energy, panel.price_kwh_sen))
        )

        self.recovery = round(self.cost / self.income, 2)

        economic_calc_buttons.append(
            data_description(f"periodo de recuperacion: {self.recovery} años",
                             calc_recovery(self.cost, self.income))
        )

        self.all_calcs = ft.Column(system_calc_descriptions + [ft.Divider(height=1)] + economic_calc_buttons)

        "---------------------------------------"
        "Identificacion del sitema y descripcion"
        "---------------------------------------"

        self.name = text_filed("Identificador del sistema", 300)
        self.description = ft.TextField(label="Descripcion", min_lines=5, max_lines=10)

        self.error = error_text("")

        self.name_and_description = ft.Column([self.name, self.description, self.error], visible=False)

        self.content = ft.Column([self.all_calcs, self.name_and_description],)

    def continue_button(self):
        if self.all_calcs.visible:
            self.all_calcs.visible = False
            self.name_and_description.visible = True
        elif self.name_and_description.visible:

            if self.name.value == "":
                self.error.visible = True
                self.error.value = "El sistema debe tener un identificador"

                self.name.color = ft.colors.RED
                self.name.label_style = ft.TextStyle(color=ft.colors.RED)

                self.update()
                return

            # Crea el sistema y guarda en la base de datos

            system = System(self.name.value, self.panel.panel_id, self.hsp_place,
                            to_south=self.to_south, description=self.description.value)
            system.save()

            system_calc = SystemCalc(system)
            system_calc.peak_power = self.peak_power_system
            system_calc.area = self.area
            system_calc.number_of_panels = self.number_of_panels
            system_calc.useful_energy = self.userful_energy
            system_calc.save()

            economic_calc = EconomicCalc(system, system_calc)
            economic_calc.income = self.income
            economic_calc.cost = self.cost
            economic_calc.recovery_period = self.recovery
            economic_calc.save()

            self.page.go('/')

        self.update()

    def back_button(self):
        if self.name_and_description.visible:
            self.all_calcs.visible = True
            self.name_and_description.visible = False

        self.update()