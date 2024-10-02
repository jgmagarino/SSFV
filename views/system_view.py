import flet as ft

from src.Mappers.calc_mapper import get_sys_calc, get_eco_calc
from src.Mappers.hsp_mapper import get_hsp
from src.Mappers.panel_mapper import get_panel
from src.modules.panel_module import Panel
from src.modules.system_module import System
from style import appbar, text_and_bg, frame, unit_of_measurement


class StaticSystem:
    _instance = None
    _system = None
    def __new__(cls):

        if cls._instance is None:
            cls._instance = super(StaticSystem, cls).__new__(cls)
        return cls._instance

    def set_system(self, system: System):
        self._system = system

    def get_system(self) -> System:
        return self._system


class UsedPanel(ft.Column):
    def __init__(self):
        super().__init__()

        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        panel: Panel = get_panel(StaticSystem().get_system().panel_id)

        self.details = ft.Column([
            ft.Row([ft.Text("Potencia pico:"), text_and_bg(f"{panel.peak_power} Wp")]),
            ft.Row([ft.Text("Material de las celdas:"), text_and_bg(f"{panel.cell_material}")]),
            ft.Row([ft.Text("Area:"), text_and_bg(f"{panel.area} m²")]),
            ft.Row([ft.Text("Precio:"), text_and_bg(f"{panel.price} cup")]),
            ft.Row([ft.Text("Precio del kwh SEN:"), text_and_bg(f"{panel.price_kwh_sen} cup")]),
        ], visible=False)

        self.controls = [
            ft.Text(f"Tipo de panel: {panel.panel_id} ", size=20),
            ft.TextButton("Detalles", on_click=self.show),
            self.details
        ]

    def show(self, e):
        self.details.visible = not self.details.visible
        self.update()


class UsedCalc(ft.Column):
    def __init__(self):
        super().__init__()

        system_calc = get_sys_calc(StaticSystem().get_system().name)

        self.controls = [
            ft.Text("Datos del sistema: ", size=20, color=ft.colors.BLUE),
            ft.Row([ft.Text(f"Energia util: {system_calc.useful_energy}"), unit_of_measurement("Wh/día")]),
            ft.Row([ft.Text(f"Numero de paneles: {system_calc.number_of_panels}")]),
            ft.Row([ft.Text(f"Area: {system_calc.area}"), unit_of_measurement("m²")]),
            ft.Row([ft.Text(f"Potencia pico: {system_calc.peak_power}"), unit_of_measurement("W")]),
        ]


class UsedEconomic(ft.Column):
    def __init__(self):
        super().__init__()

        economic_calc = get_eco_calc(StaticSystem().get_system().name)

        self.controls = [
            ft.Text("Datos economicos del sistema: ", size=20, color=ft.colors.BLUE),
            ft.Row([ft.Text(f"Costo: {economic_calc.cost}"), unit_of_measurement("CUP")]),
            ft.Row([ft.Text(f"Ingresos: {economic_calc.income}"), unit_of_measurement("CUP/año")]),
            ft.Row([ft.Text(f"Area: {economic_calc.recovery_period}"), unit_of_measurement("años")]),
        ]

class SystemView(ft.View):
    def __init__(self):
        super().__init__()

        self.route = '/system_view'
        self.appbar = appbar(StaticSystem().get_system().name)
        self.bgcolor = ft.colors.GREY_300
        self.scroll = ft.ScrollMode.ADAPTIVE
        self.auto_scroll = True

        self.edit_description = ft.IconButton(icon=ft.icons.EDIT)
        self.edit_name = ft.IconButton(icon=ft.icons.EDIT)

        self.buttons = ft.Row([
            ft.ElevatedButton("Volver", on_click=lambda e: self.page.go('/')),
            ft.ElevatedButton("Eliminar", bgcolor=ft.colors.RED, color=ft.colors.WHITE,
                              on_click=self.delete),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

        self.controls = [
            frame(UsedPanel()),
            frame(UsedCalc()),
            frame(UsedEconomic()),
            frame(ft.Text(f"Hora solar pico ({StaticSystem().get_system().place}) : "
                    f"{get_hsp(StaticSystem().get_system().place).value} h/día")),
            frame(
                ft.Column([ft.Text("Descipcion:", size=15),
                           ft.Text(StaticSystem().get_system().description)])
            ),
            frame(self.buttons),
        ]


    def delete(self, e):
        get_eco_calc(StaticSystem().get_system().name).delete()
        get_sys_calc(StaticSystem().get_system().name).delete()
        StaticSystem().get_system().delete()

        self.page.go('/')

