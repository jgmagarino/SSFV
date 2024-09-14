import flet as ft
import objects.db_querys as db
from objects.hsp import Hsp
import re


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


class CreateHsp(ft.View):
    def __init__(self):
        super().__init__()

        self.route = '/create_hsp'

        self.appbar = ft.AppBar(title=ft.Text("Insertar una nueva hora solar pico"),
                                bgcolor=ft.colors.BLUE_400, toolbar_height=100,
                                automatically_imply_leading=False)

        self.place_txt = ft.TextField(
            label="Lugar",
            border_color=ft.colors.BLUE_400,
            label_style=ft.TextStyle(color=ft.colors.BLUE_900),
            focused_border_width=3
        )

        self.place = ft.Column([self.place_txt,
                                ft.Text("Region en la que se tiene registrado "
                                           "una hora solar pico",
                                           color=ft.colors.GREY_500)
                                ], spacing=0.1)


        self.value_txt = ft.TextField(
            label="valor", border_color=ft.colors.BLUE_400,
            label_style=ft.TextStyle(color=ft.colors.BLUE_900),
            focused_border_width=3, width=100,
            on_change=only_real_numbs
        )

        self.value = ft.Row([self.value_txt,
                             ft.Container(content=ft.Text("h/día"), border_radius=10,
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
                    self.place,
                    self.value,
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

    def insert(self, e):
        is_correct, new_hsp = self.validation_empty_filed()

        if is_correct:
            err = db.insert_hsp(new_hsp)

            if err is None:
                self.page.go('/')
            else:
                self.alert_txt.value = err
                self.alert_txt.visible = True
                self.update()

        else:
            self.alert_txt.value = new_hsp
            self.alert_txt.visible = True
            self.update()


    def validation_empty_filed(self) -> (bool, Hsp | str):
        place: str = self.place_txt.value
        value: str = self.value_txt.value

        if len(place) == 0:
            self.place_txt.label_style = ft.TextStyle(color=ft.colors.RED_900)
            self.place_txt.border_color = ft.colors.RED
            return False, "Debe definir que lugar es"
        else:
            self.place_txt.label_style = ft.TextStyle(color=ft.colors.BLUE_900)
            self.place_txt.border_color = ft.colors.BLUE_400

        if len(value) == 0:
            self.value_txt.label_style = ft.TextStyle(color=ft.colors.RED_900)
            self.value_txt.border_color = ft.colors.RED
            return False, "Que valor tiene?"
        else:
            self.value_txt.label_style = ft.TextStyle(color=ft.colors.BLUE_900)
            self.value_txt.border_color = ft.colors.BLUE_400

        return True, Hsp(
            place=place,
            value=float(value),
        )






