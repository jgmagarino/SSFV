import re

import flet as ft
import objects.db_querys as db
from objects.panel import Panel


def only_real_numbs(e):
    """
    Mediante expreciones regulares compruebo que solo se escriba un numero real.
    """

    value: str = e.control.value

    if len(value) > 0:
        if value[len(value) - 1] != '.':
            if not re.match( r'^\d+(\.\d+)?$', value):
                e.control.value = value[:-1]
        else:
            if re.match(r'^\d+(\.(\d+)?)\.$', value):
                e.control.value = value[:-1]

    e.control.update()


class CreatePanel(ft.View):
    def __init__(self):
        super().__init__()

        self.route = '/create_panel'

        self.appbar = ft.AppBar(title=ft.Text("Insertar un nuevo panel"),
                                bgcolor=ft.colors.BLUE_400,
                                automatically_imply_leading=False)

        self.id_panel_txt = ft.TextField(
            label="Identificador del panel",
            border_color=ft.colors.BLUE_400,
            label_style=ft.TextStyle(color=ft.colors.BLUE_900),
            focused_border_width=3
        )

        self.id_panel = ft.Column([self.id_panel_txt,
                                   ft.Text("Puede ser un numero o un nombre, pero"
                                          " debe ser unico su valor. Ejemplo:"
                                          " Panel 1",
                                           color=ft.colors.GREY_500)
                                   ], spacing=0.1)

        self.cell_material_txt = ft.Dropdown(
            label="Material de las celdas",
            border_color=ft.colors.BLUE_400,
            label_style=ft.TextStyle(color=ft.colors.BLUE_900),
            focused_border_width=3
        )

        self.cell_material_txt.options = [ft.dropdown.Option(i.technology) for i in db.get_all_technologies()]

        self.cell_material = ft.Column([
            self.cell_material_txt,
            ft.Text("La tecnologia se define por el material en el"
                    " que estan hechas sus celdas",
                    color=ft.colors.GREY_500),
            ft.TextButton("Registrar una nueva tecnologia",
                          on_click=lambda e: self.page.go('/create_technology')),
            ft.Divider(height=1)
                                   ], spacing=0.1, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        self.peak_power_txt = ft.TextField(
            label="Potencia pico", border_color=ft.colors.BLUE_400,
            label_style=ft.TextStyle(color=ft.colors.BLUE_900),
            focused_border_width=3, width=100,
            on_change=only_real_numbs
        )

        self.peak_power = ft.Row([self.peak_power_txt,
                                  ft.Container(content=ft.Text("W"), border_radius=10,
                                               border=ft.border.all(1, ft.colors.GREY), padding=5)])

        self.area_txt = ft.TextField(
            label="Area", border_color=ft.colors.BLUE_400,
            label_style=ft.TextStyle(color=ft.colors.BLUE_900),
            focused_border_width=3, width=100,
            on_change=only_real_numbs
        )

        self.area = ft.Row([self.area_txt,
                            ft.Container(content=ft.Text("m^2"), border_radius=10,
                                         border=ft.border.all(1, ft.colors.GREY), padding=5)])

        self.price_txt = ft.TextField(
            label="Precio", border_color=ft.colors.BLUE_400,
            label_style=ft.TextStyle(color=ft.colors.BLUE_900),
            focused_border_width=3, width=100,
            on_change=only_real_numbs
        )

        self.price = ft.Row([self.price_txt,
                                  ft.Container(content=ft.Text("cup"), border_radius=10,
                                               border=ft.border.all(1, ft.colors.GREY), padding=5)])

        self.price_kwh_sen_txt = ft.TextField(
            label="Precio del Kwh SEN", border_color=ft.colors.BLUE_400,
            label_style=ft.TextStyle(color=ft.colors.BLUE_900),
            focused_border_width=3, width=100,
            on_change=only_real_numbs
        )

        self.price_kwh_sen = ft.Row([self.price_kwh_sen_txt,
                                  ft.Container(content=ft.Text("cup"), border_radius=10,
                                               border=ft.border.all(1, ft.colors.GREY), padding=5)])

        self.create = ft.ElevatedButton("Crear", bgcolor=ft.colors.BLUE_400, color=ft.colors.WHITE,
                                        on_click=self.insert)
        self.cancelate = ft.ElevatedButton("Cancelar", on_click=lambda e: self.page.go('/'))

        self.vertical_alignment = ft.MainAxisAlignment.CENTER

        self.bgcolor = ft.colors.GREY

        self.alert_txt = ft.Text("No puede haber ningun campo vacio", color=ft.colors.RED, size=20, visible=False)

        self.controls.append(

            ft.Container(
                content=ft.Row([
                    self.id_panel,
                    self.cell_material,
                    ft.Row([self.peak_power,
                    self.area], spacing=30, alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([self.price,
                            self.price_kwh_sen], spacing=30, alignment=ft.MainAxisAlignment.CENTER),
                    ft.Divider(height=1),
                    self.alert_txt,
                    ft.Row([self.create, self.cancelate], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ], wrap=True
                ),
                border_radius=5,
                padding=10,
                bgcolor=ft.colors.WHITE
            )

        )


    # Solo numeros con , o .

    def insert(self, e):
        is_correct, new_panel = self.validation_empty_filed()

        if is_correct:
            err = db.insert_panel(new_panel)

            if err is None:
                self.page.go('/')
            else:
                self.alert_txt.value = err
                self.alert_txt.visible = True
                self.update()

        else:
            self.alert_txt.value = new_panel
            self.alert_txt.visible = True
            self.update()


    def validation_empty_filed(self) -> (bool, Panel | str):
        id_panel: str = self.id_panel_txt.value
        cell_material: str  = self.cell_material_txt.value
        peak_power: str = self.peak_power_txt.value
        price: str  = self.price_txt.value
        area: str  = self.area_txt.value
        price_kwh_sen: str = self.price_kwh_sen_txt.value

        if len(id_panel) == 0:
            self.id_panel_txt.label_style = ft.TextStyle(color=ft.colors.RED_900)
            self.id_panel_txt.border_color = ft.colors.RED
            return False, "Debe definir un identificador para el panel"
        else:
            self.id_panel_txt.label_style = ft.TextStyle(color=ft.colors.BLUE_900)
            self.id_panel_txt.border_color = ft.colors.BLUE_400

        if cell_material is None:
            self.cell_material_txt.label_style = ft.TextStyle(color=ft.colors.RED_900)
            self.cell_material_txt.border_color = ft.colors.RED
            return False, "Especifique el material de las celdas"
        else:
            self.cell_material_txt.label_style = ft.TextStyle(color=ft.colors.BLUE_900)
            self.cell_material_txt.border_color = ft.colors.BLUE_400

        if len(peak_power) == 0:
            self.peak_power_txt.label_style = ft.TextStyle(color=ft.colors.RED_900)
            self.peak_power_txt.border_color = ft.colors.RED
            return False, "Que potencia pico tiene el panel?"
        else:
            self.peak_power_txt.label_style = ft.TextStyle(color=ft.colors.BLUE_900)
            self.peak_power_txt.border_color = ft.colors.BLUE_400

        if len(price) == 0:
            self.price_txt.label_style = ft.TextStyle(color=ft.colors.RED_900)
            self.price_txt.border_color = ft.colors.RED
            return False, "Cuanto cuesta el panel?"
        else:
            self.price_txt.label_style = ft.TextStyle(color=ft.colors.BLUE_900)
            self.price_txt.border_color = ft.colors.BLUE_400

        if len(area) == 0:
            self.area_txt.label_style = ft.TextStyle(color=ft.colors.RED_900)
            self.area_txt.border_color = ft.colors.RED
            return False, "Que area ocupa cada panel?"
        else:
            self.area_txt.label_style = ft.TextStyle(color=ft.colors.BLUE_900)
            self.area_txt.border_color = ft.colors.BLUE_400

        if len(price_kwh_sen) == 0:
            self.price_kwh_sen_txt.label_style=ft.TextStyle(color=ft.colors.RED_900)
            self.price_kwh_sen_txt.border_color=ft.colors.RED
            return False, "price_kwh_sen:empty"
        else:
            self.price_kwh_sen_txt.label_style = ft.TextStyle(color=ft.colors.BLUE_900)
            self.price_kwh_sen_txt.border_color=ft.colors.BLUE_400

        return True, Panel(
            id_panel=id_panel,
            cell_material=cell_material,
            peak_power=float(peak_power),
            price=float(price),
            area=float(area),
            price_kwh_sen=float(price_kwh_sen),
        )









