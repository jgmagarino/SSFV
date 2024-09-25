import flet as ft

from validation import only_real_numbs
from style import (text_filed, error_text, frame, unit_of_measurement, appbar)
from src.modules.hsp_module import HSP


class CreateHsp(ft.View):
    def __init__(self):
        super().__init__()

        "-----------"
        "PROPIEDADES"
        "-----------"

        self.route = '/create_hsp'
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.bgcolor = ft.colors.GREY_300

        "-----------"
        "COMPONENTES"
        "-----------"

        self.appbar = appbar("Nueva hora solar pico")

        self.place_tf = text_filed("Lugar", 300)

        self.place = ft.Column([self.place_tf,
                                ft.Text("Region en la que se tiene registrado "
                                           "una hora solar pico",
                                           color=ft.colors.GREY_500)
                                ], spacing=0.1)


        self.value_tf = text_filed("Valor")
        self.value_tf.on_change=only_real_numbs

        self.create = ft.ElevatedButton("Crear", bgcolor=ft.colors.BLUE_400, color=ft.colors.WHITE,
                                        on_click=self.insert)

        self.cancelate = ft.ElevatedButton("Cancelar", on_click=lambda e: self.page.go('back'))

        self.alert = error_text("No puede haber ningun campo vacio.")

        "----------"
        "ESTRUCTURA"
        "----------"

        self.controls.append(
           frame(
                content=ft.Row(
                    [
                        self.place,
                        ft.Row([self.value_tf, unit_of_measurement("h/dia")]),
                        ft.Divider(height=1),
                        self.alert,
                        ft.Row([self.create, self.cancelate],
                               alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ], wrap=True
                ),
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
        is_correct, new_hsp = self.validation_empty_filed()

        if is_correct:
            
            self.page.go('back')

        else:
            self.alert.value = "Error"
            self.alert.visible = True
            self.update()

        self.alert.value = new_hsp
        self.alert.visible = True
        self.update()


    def validation_empty_filed(self) -> (bool, HSP | str):
        """
        Se asegura de que los text filed no esten vacios
        :return : una tupla (verdadero y la nueva hsp o falso y mensaje de error si hay algun campo vacio)
        """
        place: str = self.place_tf.value
        value: str = self.value_tf.value

        if len(place) == 0:
            self.place_tf.label_style = ft.TextStyle(color=ft.colors.RED_900)
            self.place_tf.border_color = ft.colors.RED
            return False, "Debe definir que lugar es"
        else:
            self.place_tf.label_style = ft.TextStyle(color=ft.colors.BLUE_900)
            self.place_tf.border_color = ft.colors.BLUE_400

        if len(value) == 0:
            self.value_tf.label_style = ft.TextStyle(color=ft.colors.RED_900)
            self.value_tf.border_color = ft.colors.RED
            return False, "Que valor tiene?"
        else:
            self.value_tf.label_style = ft.TextStyle(color=ft.colors.BLUE_900)
            self.value_tf.border_color = ft.colors.BLUE_400

        return True, HSP(place=place, value=float(value))






