import flet as ft

from src.modules.panel_module import Panel
from style import text_and_bg, unit_of_measurement


def show_row(atr: str, info, unit=None):
    return ft.Row([text_and_bg(atr), ft.Text(info), unit_of_measurement(unit) if unit else ft.Text("")])

class ShowPanel(ft.Container):
    def __init__(self, panel: Panel):
        super().__init__()

        self.panel = panel

        self.bgcolor = ft.colors.WHITE
        self.padding = 10
        self.border_radius = 10
        self.border = ft.border.all(1, ft.colors.GREY)
        self.width = 300

        column = ft.Column([
            show_row("Potencia pico: ", panel.peak_power, "W"),
            show_row("Material de las celdas: ", panel.cell_material),
            show_row("Area: ", panel.area, "m^2"),
            show_row("Price: ", panel.price, "cup"),
            show_row("Precio del kwh SEN: ", panel.price_kwh_sen, "cup")
        ])

        self.more_info = ft.Row([column], scroll=ft.ScrollMode.ADAPTIVE, visible=False)

        self.content = ft.Column([
            ft.Text(panel.panel_id, size=20),
            self.more_info,
            ft.Divider(height=1),
            ft.Row([ft.ElevatedButton("Detalles", on_click=self.show_details),
                    ft.ElevatedButton("Eliminar", bgcolor=ft.colors.RED, on_click=self.remove)],
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
        self.panel.visible = 0
        self.panel.delete()
        self.panel.save()
        self.visible = False
        self.update()





