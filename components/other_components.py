from platform import system
from xml.dom.minidom import Entity

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


class EntityInfo(ft.Container):
    def __init__(self, entity: Panel | Hsp | Technology):
        super().__init__()

        if isinstance(entity, Panel):
            self.entity: Panel = entity

            peak_power = info_container("potencia pico", self.entity.peak_power)
            cell_material = info_container("material de las celdas", self.entity.cell_material)
            area = info_container("area", self.entity.area)
            price = info_container("precio", self.entity.price)
            price_kwh_sen = info_container("precio del kwh SEN", self.entity.price_kwh_sen)

            self.info = [peak_power, cell_material, area, price, price_kwh_sen]

        if isinstance(entity, Hsp):
            self.entity: Hsp = entity

            place = info_container("lugar", self.entity.place)
            value = info_container("valor", self.entity.value)

            self.info = [place, value]

        if isinstance(entity, Technology):
            self.entity: Technology = entity

            peak_power = info_container("tecnologia", self.entity.technology)
            cell_material = info_container("area requerida", self.entity.surface)

            self.info = [peak_power, cell_material]

        # bordes y padding
        self.border = ft.border.all(1, ft.colors.GREY)
        self.border_radius = 5
        self.padding = 10

        self.content = ft.Row(self.info, wrap=True)


class WhereUsed(ft.Container):
    def __init__(self, entity: Panel | Hsp | Technology):
        super().__init__()

        systems = []

        if isinstance(entity, Panel):
            self.entity: Panel = entity

            systems = DatabaseConnection().find_panel(self.entity.id_panel)

        if isinstance(entity, Hsp):
            self.entity: Hsp = entity

            systems = DatabaseConnection().find_hsp(self.entity.place)

        if isinstance(entity, Technology):
            self.entity: Technology = entity

            systems = DatabaseConnection().find_technology(self.entity.technology)

        # bordes y padding
        self.border = ft.border.all(1, ft.colors.GREY)
        self.border_radius = 5
        self.padding = 10

        if systems:
            pass
        else:
            self.content = ft.Text("No se usa en ningun sistema.")