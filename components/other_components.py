import flet as ft


from src.modules.panel_module import Panel
from src.modules.hsp_module import HSP
from src.modules.technology_module import Technology
from style import (text_and_bg, unit_of_measurement)


def info_container(info: str, value, unit=None):
    return ft.Row([
        text_and_bg(text=info),
        ft.Text(value, size=15),
        unit if unit is not None else ft.Text(""),
    ])


class EntityInfo(ft.Container):
    def __init__(self, entity: Panel | HSP | Technology):
        """
        Mustra la informacion de los atributos de la entidad.

        :param entity: entidad a mostrar
        """

        super().__init__()

        "-----------"
        "PROPIEDADES"
        "-----------"

        self.border = ft.border.all(1, ft.colors.GREY)
        self.border_radius = 5
        self.padding = 10

        "----------"
        "ESTRUCTURA"
        "----------"

        self.info = []

        # Panel
        if isinstance(entity, Panel):
            self.entity: Panel = entity

            # Atributos
            technology = info_container("potencia pico", self.entity.peak_power, unit_of_measurement("W"))
            cell_material = info_container("material de las celdas", self.entity.cell_material)
            area = info_container("area", self.entity.area, unit_of_measurement("m^2"))
            price = info_container("precio", self.entity.price, unit_of_measurement("cup"))
            price_kwh_sen = info_container("precio del kwh SEN", self.entity.price_kwh_sen,
                                           unit_of_measurement("cup"))

            self.info = [technology, cell_material, area, price, price_kwh_sen]

        # Hora solar pico
        if isinstance(entity, HSP):
            self.entity: HSP = entity

            # Atributos
            place = info_container("lugar", self.entity.place)
            value = info_container("valor", self.entity.value, unit_of_measurement("h/día"))

            self.info = [place, value]

        # Tecnologia
        if isinstance(entity, Technology):
            self.entity: Technology = entity

            # Atributos
            technology = info_container("tecnologia", self.entity.technology)
            area = info_container("area requerida",
                                           f"{self.entity.convert_to_number()[0]} - {self.entity.convert_to_number()[1]}",
                                  unit_of_measurement("m^2"))

            self.info = [technology, area]

        self.content = ft.Row([ft.Column(self.info)], scroll=ft.ScrollMode.ADAPTIVE)


class WhereUsed(ft.Container):
    def __init__(self, entity: Panel | HSP):
        """
        Muestra los sistemas donde se usa esta entidad.

        :param entity:
        """
        super().__init__()

        "-----------"
        "PROPIEDADES"
        "-----------"

        self.border = ft.border.all(1, ft.colors.GREY)
        self.border_radius = 5
        self.padding = 10

        if isinstance(entity, Panel) or isinstance(entity, HSP):
            systems = [ft.Text(i.name) for i in entity.get_system()]
        else:
            systems = None

        if systems:
            self.content = ft.Column(systems)
        else:
            self.content = ft.Text("No se usa en ningun sistema.")