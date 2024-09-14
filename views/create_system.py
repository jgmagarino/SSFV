import flet as ft
from components.create_system_components import (SelectPlace, SelectPanel, SpecificData, CalcWithArea,
                                                 CalcWithPeakPower, Economic, FinalFace)


class CreateSystem(ft.View):
    def __init__(self):
        super().__init__()

        self.route = '/create_system'
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.bgcolor = ft.colors.GREY_300

        self.appbar = ft.AppBar(title=ft.Text("Crear un sistema"),
                                bgcolor=ft.colors.BLUE_400,
                                automatically_imply_leading=False)

        self.progress = 0


        self.button_back = ft.ElevatedButton("Atras", on_click=self.back)
        self.button_continue = ft.ElevatedButton("Calcular", on_click=self.create_system,
                                                 bgcolor=ft.colors.BLUE, color=ft.colors.WHITE)

        self.selected_place = SelectPlace()
        self.selected_panel = SelectPanel()
        self.exact_calc = SpecificData()

        self.error_message = ft.Text("", color=ft.colors.RED, size=20, visible=False)

        self.content = ft.Container(
            content=ft.Column([
                ft.Column([self.selected_place, self.selected_panel, self.exact_calc,
                ft.Divider(height=1),
                self.error_message,
                ft.Row([self.button_back, self.button_continue], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)]),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.WHITE,
            border_radius=5,
            padding=10,
        )

        self.face = 0

        self.scroll = ft.ScrollMode.ADAPTIVE
        self.auto_scroll = True

        self.controls.append(self.content)


    def validation(self, e):

        if self.selected_panel.get_selected_panel() is None:
            self.selected_panel.set_error()
            self.error_message.visible = True
            self.error_message.value = "Tiene que seleccionar un panel para continuar"
        else:
            self.error_message.visible = False
            self.selected_panel.set_normal()

        self.update()

    def back(self, e):
        if self.face == 0:
            self.page.go('/')

        if self.face == 1:
            self.content.content = ft.Column([
                ft.Column([self.selected_place, self.selected_panel, self.exact_calc,
                ft.Divider(height=1),
                self.error_message,
                ft.Row([self.button_back, self.button_continue], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)]),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

            self.face -= 1
            self.button_continue.text = "Calcular"

        self.update()

    def create_system(self, e):
        if self.face == 0:

            if self.exact_calc.is_specific_area:
                calc = CalcWithArea(self.exact_calc.get_value(), self.selected_panel.get_selected_panel(),
                                    self.selected_place.get_hsp(), self.exact_calc.to_south.value)
            else:
                calc = CalcWithPeakPower(self.exact_calc.get_value(), self.selected_panel.get_selected_panel(),
                                  self.selected_place.get_hsp(), self.exact_calc.to_south)

            self.content.content = ft.Column([
                calc,
                Economic(self.selected_panel.get_selected_panel(), calc.number_of_panels_value,
                         calc.userful_energy_value),
                ft.Divider(height=1),
                ft.Row([self.button_back, self.button_continue],
                       alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

            self.face += 1
            self.button_continue.text = "Guardar Calculos"

        elif self.face == 1:
            self.content.content = ft.Column([
                FinalFace(),
                ft.Divider(height=1),
                ft.Row([self.button_back, self.button_continue],
                       alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

            self.button_continue.text = "Guardar sistema"

        self.update()
