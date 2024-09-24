import flet as ft

import objects.db_querys as db

from objects.panel import Panel
from validation import only_real_numbs
from style import (appbar, text_filed, dropdown, unit_of_measurement, error_text, frame)


class CreatePanel(ft.View):
    def __init__(self):
        super().__init__()

        "-----------"
        "PROPIEDADES"
        "-----------"

        self.route = '/create_panel'
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.bgcolor = ft.colors.GREY_300

        "-----------"
        "COMPONENTES"
        "-----------"

        self.appbar = appbar("Nuevo panel")

        self.id_panel_tf = text_filed("Identificador del panel", 300)

        self.id_panel = ft.Column([self.id_panel_tf,
                                   ft.Text("Puede ser un numero o un nombre, pero"
                                          " debe ser unico su valor. Ejemplo:"
                                          " Panel 1",
                                           color=ft.colors.GREY_500)
                                   ], spacing=0.1)

        self.cell_material_dropdown = dropdown(
            "Material de las celdas",
            [ft.dropdown.Option(i.technology) for i in db.get_all_technologies()],
            400
        )

        self.cell_material = ft.Column([
            self.cell_material_dropdown,
            ft.Text("La tecnologia se define por el material en el"
                    " que estan hechas sus celdas",
                    color=ft.colors.GREY_500),
            ft.TextButton("Registrar una nueva tecnologia",
                          on_click=lambda e: self.page.go('/create_technology')),
            ],
            spacing=0.1, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        self.peak_power_tf = text_filed("Potencia pico")
        self.peak_power_tf.on_change=only_real_numbs
        self.peak_power = ft.Row([self.peak_power_tf, unit_of_measurement("W")])

        self.area_tf = text_filed("Area")
        self.area_tf.on_change=only_real_numbs
        self.area = ft.Row([self.area_tf, unit_of_measurement("m^2")])

        self.price_tf = text_filed("Precio")
        self.price_tf.on_change=only_real_numbs
        self.price = ft.Row([self.price_tf, unit_of_measurement("cup")])

        self.price_kwh_sen_tf = text_filed("Precio del kwh SEN")
        self.price_kwh_sen = ft.Row([self.price_kwh_sen_tf, unit_of_measurement("cup")])

        self.create = ft.ElevatedButton("Crear", bgcolor=ft.colors.BLUE_400, color=ft.colors.WHITE,
                                        on_click=self.insert)
        self.cancelate = ft.ElevatedButton("Cancelar", on_click=lambda e: self.page.go('/'))

        self.alert_txt = error_text("No puede haber ningun campo vacio")

        "----------"
        "ESTRUCTURA"
        "----------"

        numeric_camps = ft.Row([
            ft.Column([self.peak_power, self.price]),
            ft.Column([self.area, self.price_kwh_sen]),
        ])

        self.controls.append(

            frame(
                content=ft.Column([
                    self.id_panel,
                    self.cell_material,
                    ft.Divider(height=1),
                    numeric_camps,
                    ft.Divider(height=1),
                    self.alert_txt,
                    ft.Row([self.create, self.cancelate],
                           alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ])
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
        """
        Se asegura de que los text filed no esten vacios
        :return : una tupla (verdadero y la nueva hsp o falso y mensaje de error si hay algun campo vacio)
        """

        id_panel: str = self.id_panel_tf.value
        cell_material: str  = self.cell_material_dropdown.value
        peak_power: str = self.peak_power_tf.value
        price: str  = self.price_tf.value
        area: str  = self.area_tf.value
        price_kwh_sen: str = self.price_kwh_sen_tf.value

        if len(id_panel) == 0:
            self.id_panel_tf.label_style = ft.TextStyle(color=ft.colors.RED_900)
            self.id_panel_tf.border_color = ft.colors.RED
            return False, "Debe definir un identificador para el panel"
        else:
            self.id_panel_tf.label_style = ft.TextStyle(color=ft.colors.BLUE_900)
            self.id_panel_tf.border_color = ft.colors.BLUE_400

        if cell_material is None:
            self.cell_material_dropdown.label_style = ft.TextStyle(color=ft.colors.RED_900)
            self.cell_material_dropdown.border_color = ft.colors.RED
            return False, "Especifique el material de las celdas"
        else:
            self.cell_material_dropdown.label_style = ft.TextStyle(color=ft.colors.BLUE_900)
            self.cell_material_dropdown.border_color = ft.colors.BLUE_400

        if len(peak_power) == 0:
            self.peak_power_tf.label_style = ft.TextStyle(color=ft.colors.RED_900)
            self.peak_power_tf.border_color = ft.colors.RED
            return False, "Que potencia pico tiene el panel?"
        else:
            self.peak_power_tf.label_style = ft.TextStyle(color=ft.colors.BLUE_900)
            self.peak_power_tf.border_color = ft.colors.BLUE_400

        if len(price) == 0:
            self.price_tf.label_style = ft.TextStyle(color=ft.colors.RED_900)
            self.price_tf.border_color = ft.colors.RED
            return False, "Cuanto cuesta el panel?"
        else:
            self.price_tf.label_style = ft.TextStyle(color=ft.colors.BLUE_900)
            self.price_tf.border_color = ft.colors.BLUE_400

        if len(area) == 0:
            self.area_tf.label_style = ft.TextStyle(color=ft.colors.RED_900)
            self.area_tf.border_color = ft.colors.RED
            return False, "Que area ocupa cada panel?"
        else:
            self.area_tf.label_style = ft.TextStyle(color=ft.colors.BLUE_900)
            self.area_tf.border_color = ft.colors.BLUE_400

        if len(price_kwh_sen) == 0:
            self.price_kwh_sen_tf.label_style=ft.TextStyle(color=ft.colors.RED_900)
            self.price_kwh_sen_tf.border_color=ft.colors.RED
            return False, "price_kwh_sen:empty"
        else:
            self.price_kwh_sen_tf.label_style = ft.TextStyle(color=ft.colors.BLUE_900)
            self.price_kwh_sen_tf.border_color=ft.colors.BLUE_400

        return True, Panel(
            id_panel=id_panel,
            cell_material=cell_material,
            peak_power=float(peak_power),
            price=float(price),
            area=float(area),
            price_kwh_sen=float(price_kwh_sen),
        )









