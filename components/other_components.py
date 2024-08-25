import flet as ft

from db_gestor import DatabaseConnection
from objects.hsp import Hsp
from objects.panel import Panel
from objects.technology import Technology


# todo arreglar esto para los textos que no quepan en pantalla
def info_container(info: str, value):
    return ft.Row([
        ft.Container(content=ft.Text(f"{info} :", size=15),
                     bgcolor=ft.colors.BLUE_100, padding=5, border_radius=5),
        ft.Text(value, size=15)
    ])


class PanelInfo(ft.Container):
    def __init__(self, panel: Panel):
        super().__init__()

        self.panel: Panel = panel

        # bordes y padding
        self.border = ft.border.all(1, ft.colors.GREY)
        self.border_radius = 5
        self.padding = 10

        # informacion
        peak_power = info_container("potencia pico", self.panel.peak_power)
        cell_material = info_container("material de las celdas", self.panel.cell_material)
        area = info_container("area", self.panel.area)
        price = info_container("precio", self.panel.price)
        price_kwh_sen = info_container("precio del kwh SEN", self.panel.price_kwh_sen)

        self.content = ft.Row([
            peak_power,
            cell_material,
            area,
            price,
            price_kwh_sen
        ],wrap=True)


class PanelOnSystem(ft.Container):
    def __init__(self, panel):
        super().__init__()

        self.panel: Panel = panel

        # bordes y padding
        self.border = ft.border.all(1, ft.colors.GREY)
        self.border_radius = 5
        self.padding = 10

        systems = DatabaseConnection().find_panel(self.panel.id_panel)

        if systems:
            pass
        else:
            self.content = ft.Text("No hay sistemas que usen este tipo panel")


class HspInfo(ft.Container):
    def __init__(self, hsp: Hsp):
        super().__init__()

        self.hsp: Hsp = hsp

        # bordes y padding
        self.border = ft.border.all(1, ft.colors.GREY)
        self.border_radius = 5
        self.padding = 10

        # informacion
        peak_power = info_container("lugar", self.hsp.place)
        cell_material = info_container("valor", self.hsp.value)

        self.content = ft.Row([
            peak_power,
            cell_material,
        ],wrap=True)


class HspOnSystem(ft.Container):
    def __init__(self, hsp: Hsp):
        super().__init__()

        self.hsp: Hsp = hsp

        # bordes y padding
        self.border = ft.border.all(1, ft.colors.GREY)
        self.border_radius = 5
        self.padding = 10

        systems = DatabaseConnection().find_hsp(self.hsp.place)

        if systems:
            pass
        else:
            self.content = ft.Text("No hay sistemas en este lugar especifico")


class TechnologyInfo(ft.Container):
    def __init__(self, technology: Technology):
        super().__init__()

        self.technology: Technology = technology

        # bordes y padding
        self.border = ft.border.all(1, ft.colors.GREY)
        self.border_radius = 5
        self.padding = 10

        # informacion
        peak_power = info_container("tecnologia", self.technology.technology)
        cell_material = info_container("area requerida", self.technology.surface)

        self.content = ft.Row([
            peak_power,
            cell_material,
        ],wrap=True)


class TechnologyOnSystem(ft.Container):
    def __init__(self, technology: Technology):
        super().__init__()

        self.technology: Technology = technology

        # bordes y padding
        self.border = ft.border.all(1, ft.colors.GREY)
        self.border_radius = 5
        self.padding = 10

        systems = DatabaseConnection().find_technology(self.technology.technology)

        if systems:
            pass
        else:
            self.content = ft.Text("No hay sistemas en este lugar especifico")