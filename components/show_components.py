import flet as ft

from src.modules.hsp_module import HSP
from src.modules.panel_module import Panel
from src.modules.system_module import System
from src.modules.technology_module import Technology
from style import text_and_bg, unit_of_measurement, frame
from views.system_view import (SystemView, StaticSystem)


def show_row(atr: str, info, unit=None):
    return ft.Row([text_and_bg(atr), ft.Text(info), unit_of_measurement(unit) if unit else ft.Text("")])

def get_details(entity: HSP | Panel):

    frame_systems = ft.Text("")

    used_systems = []

    if not isinstance(entity, Technology):

        used_systems = entity.get_system()

        frame_systems = frame(ft.Column( [text_and_bg("Se usa en: ")] +
                                 [text_and_bg(i.name, ft.colors.GREY) for i in used_systems]))
        frame_systems.border = ft.border.all(1, ft.colors.GREY)

    if isinstance(entity, HSP):
        return ft.Column([
            show_row("Value: ", entity.value, "h/día"),
            ft.Divider(height=1),
            frame_systems
        ]), False if not used_systems else True

    if isinstance(entity, Panel):
        return ft.Column([
            show_row("Potencia pico: ", entity.peak_power, "W"),
            show_row("Material de las celdas: ", entity.cell_material),
            show_row("Area: ", entity.area, "m^2"),
            show_row("Price: ", entity.price, "cup"),
            show_row("Precio del kwh SEN: ", entity.price_kwh_sen, "cup"),
            ft.Divider(height=1),
            frame_systems
        ]), False if not used_systems else True

    if isinstance(entity, Technology):
        return ft.Column([
            show_row("Area requerida: ", entity.surface),
        ]), False if not used_systems else True


class ShowEntity(ft.Container):
    def __init__(self, entity: Panel | HSP | Technology):
        super().__init__()

        self.entity = entity

        self.bgcolor = ft.colors.WHITE
        self.padding = 10
        self.border_radius = 10
        self.border = ft.border.all(1, ft.colors.GREY)
        self.width = 300

        details, used_systems = get_details(entity)

        self.more_info = ft.Row([details],
                                scroll=ft.ScrollMode.ADAPTIVE, visible=False)

        title = ""

        if isinstance(entity, HSP):
            title = entity.place
        elif isinstance(entity, Panel):
            title = entity.panel_id
        elif isinstance(entity, Technology):
            title = entity.technology

        self.content = ft.Column([
            ft.Text(title, size=20),
            self.more_info,
            ft.Divider(height=1),
            ft.Row([ft.ElevatedButton("Detalles", on_click=self.show_details),
                    ft.ElevatedButton("Eliminar", bgcolor=ft.colors.RED, on_click=self.remove
                                      , disabled=True if used_systems else False),],
                   alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def show_details(self, e):
        self.more_info.visible = not self.more_info.visible

        if self.more_info.visible:
            self.border = ft.border.all(3, ft.colors.BLUE)
        else:
            self.border = ft.border.all(1, ft.colors.GREY)

        self.update()

    def remove(self, e):
        self.visible = False
        self.update()

        self.entity.visible = 0
        self.entity.delete()


class ShowSystem(ft.Container):
    def __init__(self, system: System):
        super().__init__()

        self.system = system

        self.bgcolor = ft.colors.WHITE
        self.padding = 10
        self.border_radius = 10
        self.border = ft.border.all(1, ft.colors.GREY)
        self.width = 300

        go_to_details = ft.ElevatedButton("Ver detalles", on_click=self.show_system)

        self.content = ft.Column([
            ft.Text(system.name, size=20),
            go_to_details,
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def show_system(self, e):
        StaticSystem().set_system(self.system)
        self.page.go('/system_view')
