import flet as ft
import objects.db_querys as db
from objects.technology import Technology
from style import (appbar, text_filed, unit_of_measurement, error_text, frame)


class CreateTechnology(ft.View):
    def __init__(self):
        super().__init__()

        "-----------"
        "PROPIEDADES"
        "-----------"

        self.route = '/create_technology'
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.bgcolor = ft.colors.GREY_300

        "-----------"
        "COMPONENTES"
        "-----------"

        self.appbar = appbar("Insertar una nueva tecnologia")

        self.technology_tf = text_filed("Tecnologia", 300)
        self.technology = ft.Column([self.technology_tf,
                                     ft.Text("Identificador de la tecnologia, puede ser un nombre, un"
                                             "numero o el material de la misma.",
                                             color=ft.colors.GREY_500)
                                     ], spacing=0.1)

        self.surface_tf_1 = text_filed(width=70)
        self.surface_tf_2 = text_filed(width=70)
        self.surface = ft.Column([
            ft.Text("Area:", style=ft.TextStyle(color=ft.colors.BLUE_900)),
            ft.Row([self.surface_tf_1, ft.Text("-"), self.surface_tf_2, unit_of_measurement("m^2")]),
            ft.Text("Rango del area requerida para la generacion de 1 kw con esta tecnologia"
                    " en especifico.",
                    color=ft.colors.GREY_500)
        ])

        self.create = ft.ElevatedButton("Crear", bgcolor=ft.colors.BLUE_400, color=ft.colors.WHITE,
                                        on_click=self.insert)
        self.cancelate = ft.ElevatedButton("Cancelar", on_click=lambda e: self.page.go('/'))

        self.alert = error_text("No puede haber ningun campo vacio")

        "----------"
        "ESTRUCTURA"
        "----------"

        self.controls.append(

            frame(
                content=ft.Column([
                    self.technology,
                    self.surface,
                    ft.Divider(height=1),
                    self.alert,
                    ft.Row([self.create, self.cancelate],
                           alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ]
                )
            )

        )

    "------"
    "EVENTO"
    "------"

    def insert(self, e):
        """
        Evento, inserta una nueva hora solar pico si la validacion es correcta y no hay error
        a la hora de insertar en la base de datos, en caso contrario muestra una alerta inducando
        el error.
        """
        is_correct, new_technology = self.validation_empty_filed()

        if is_correct:
            err = db.insert_technology(new_technology)

            if err is None:
                self.page.go('/')
            else:
                self.alert.value =err
                self.alert.visible = True
                self.update()

        else:
            self.alert.value = new_technology
            self.alert.visible = True
            self.update()


    def validation_empty_filed(self) -> (bool, Technology | str):
        """
        Se asegura de que los text filed no esten vacios
        :return : una tupla (verdadero y la nueva hsp o falso y mensaje de error si hay algun campo vacio)
        """

        technology: str = self.technology_tf.value
        surface: tuple[str, str] = self.surface_tf_1.value, self.surface_tf_2.value

        if len(technology) == 0:
            self.technology_tf.label_style = ft.TextStyle(color=ft.colors.RED_900)
            self.technology_tf.border_color = ft.colors.RED
            return False, "Que tipo de tecnologia es?"
        else:
            self.technology_tf.label_style = ft.TextStyle(color=ft.colors.BLUE_900)
            self.technology_tf.border_color = ft.colors.BLUE_400

        if len(surface[0]) == 0 or len(surface[1]) == 0:
            self.surface_tf_1.label_style = ft.TextStyle(color=ft.colors.RED_900)
            self.surface_tf_1.border_color = ft.colors.RED

            self.surface_tf_2.label_style = ft.TextStyle(color=ft.colors.RED_900)
            self.surface_tf_2.border_color = ft.colors.RED

            return False, "Que superficie requiere?"
        else:
            self.surface_tf_1.label_style = ft.TextStyle(color=ft.colors.BLUE_900)
            self.surface_tf_1.border_color = ft.colors.BLUE_400

            self.surface_tf_2.label_style = ft.TextStyle(color=ft.colors.BLUE_900)
            self.surface_tf_2.border_color = ft.colors.BLUE_400

        return True, Technology(
            technology=technology,
            surface=f"{surface[0]} - {surface[1]}",
        )


