import flet as ft
import objects.db_querys as db
from objects.technology import Technology


class CreateTechnology(ft.View):
    def __init__(self):
        super().__init__()

        self.route = '/create_technology'

        self.appbar = ft.AppBar(title=ft.Text("Insertar una nueva tecnologia"),
                                bgcolor=ft.colors.BLUE_400, toolbar_height=100,
                                automatically_imply_leading=False)

        self.technology_txt = ft.TextField(
            label="Tecnologia",
            border_color=ft.colors.BLUE_400,
            label_style=ft.TextStyle(color=ft.colors.BLUE_900),
            focused_border_width=3
        )

        self.surface_txt_1 = ft.TextField(
            border_color=ft.colors.BLUE_400,
            label_style=ft.TextStyle(color=ft.colors.BLUE_900),
            focused_border_width=3, width=80,
            input_filter=ft.NumbersOnlyInputFilter()
        )

        self.surface_txt_2 = ft.TextField(
            border_color=ft.colors.BLUE_400,
            label_style=ft.TextStyle(color=ft.colors.BLUE_900),
            focused_border_width=3, width=80,
            input_filter=ft.NumbersOnlyInputFilter()
        )

        self.technology = ft.Column([self.technology_txt,
                                     ft.Text("Identificador de la tecnologia, puede ser un nombre, un"
                                             "numero o el material de la misma.",
                                           color=ft.colors.GREY_500)
                                     ], spacing=0.1)


        self.surface = ft.Column([
            ft.Text("Area:", style=ft.TextStyle(color=ft.colors.BLUE_900)),
            ft.Row([self.surface_txt_1, ft.Text("-"), self.surface_txt_2,
                    ft.Container(content=ft.Text("m^2"), border_radius=10,
                    border=ft.border.all(1, ft.colors.GREY), padding=5)]),
            ft.Text("Rango del area requerida para la generacion de 1 kw con esta tecnologia"
                    "en especifico.",
                    color=ft.colors.GREY_500)
        ])


        self.create = ft.ElevatedButton("Crear", bgcolor=ft.colors.BLUE_400, color=ft.colors.WHITE,
                                        on_click=self.insert)
        self.cancelate = ft.ElevatedButton("Cancelar", on_click=lambda e: self.page.go('/'))

        self.vertical_alignment = ft.MainAxisAlignment.CENTER

        self.bgcolor = ft.colors.GREY

        self.alert_txt = ft.Text("No puede haber ningun campo vacio", color=ft.colors.RED, size=20, visible=False)

        self.controls.append(

            ft.Container(
                content=ft.Row([
                    self.technology,
                    self.surface,
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
        is_correct, new_technology = self.validation_empty_filed()

        if is_correct:
            err = db.insert_technology(new_technology)

            if err is None:
                self.page.go('/')
            else:
                self.alert_txt.value =err
                self.alert_txt.visible = True
                self.update()

        else:
            self.alert_txt.value = new_technology
            self.alert_txt.visible = True
            self.update()



    def validation_empty_filed(self) -> (bool, Technology | str):
        technology: str = self.technology_txt.value
        surface: tuple[str, str] = self.surface_txt_1.value, self.surface_txt_2.value

        if len(technology) == 0:
            self.technology_txt.label_style = ft.TextStyle(color=ft.colors.RED_900)
            self.technology_txt.border_color = ft.colors.RED
            return False, "Que tipo de tecnologia es?"
        else:
            self.technology_txt.label_style = ft.TextStyle(color=ft.colors.BLUE_900)
            self.technology_txt.border_color = ft.colors.BLUE_400

        if len(surface[0]) == 0 or len(surface[1]) == 0:
            self.surface_txt_1.label_style = ft.TextStyle(color=ft.colors.RED_900)
            self.surface_txt_1.border_color = ft.colors.RED

            self.surface_txt_2.label_style = ft.TextStyle(color=ft.colors.RED_900)
            self.surface_txt_2.border_color = ft.colors.RED

            return False, "Que superficie requiere?"
        else:
            self.surface_txt_1.label_style = ft.TextStyle(color=ft.colors.BLUE_900)
            self.surface_txt_1.border_color = ft.colors.BLUE_400

            self.surface_txt_2.label_style = ft.TextStyle(color=ft.colors.BLUE_900)
            self.surface_txt_2.border_color = ft.colors.BLUE_400

        return True, Technology(
            technology=technology,
            surface=f"{surface[0]} - {surface[1]}",
        )


