import flet as ft
from components.create_system_components import (SelectPlace, SelectPanel, SpecificData)
from components.system_calc import Calc
from src.Mappers.panel_mapper import get_panel
from style import (appbar, error_text, frame)

class CreateSystem(ft.View):
    def __init__(self):
        super().__init__()

        self.route = '/create_system'
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.bgcolor = ft.colors.GREY_300
        self.scroll = ft.ScrollMode.ADAPTIVE
        self.auto_scroll = True

        self.appbar = appbar("Crear un sistema")

        self.calculate_button = ft.ElevatedButton("Calcular", bgcolor=ft.colors.BLUE,
                                                  color=ft.colors.WHITE, on_click=self.continue_button)

        self.back_button = ft.ElevatedButton("Atras", on_click=lambda e: self.page.go('/'))

        self.buttons = ft.Row([self.back_button, self.calculate_button],
                              alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

        self.hsp = SelectPlace()
        self.panel = SelectPanel()
        self.specific_data = SpecificData()
        self.error = error_text("")

        self.form_frame = frame(
            ft.Column([
                self.hsp,
                self.panel,
                self.specific_data,
                ft.Divider(height=1),
                self.error,
                self.buttons
            ])
        )

        self.calc_frame = None

        self.controls.append(self.form_frame)

    def validation_form(self) -> bool:
        if self.panel.get_selected_panel() is None:
            self.error.value = "Debe seleccionar un panel"
            self.error.visible = True
            self.panel.set_error()
            self.update()
            return False
        else:
            self.panel.set_normal()

        if self.specific_data.get_value() == "":
            self.error.value = "Debe definir un area o una potencia a instalar"
            self.error.visible = True
            self.specific_data.set_error()
            self.update()
            return False
        else:
            self.specific_data.set_normal()

        self.update()
        return True

    def continue_button(self, e):
        if self.calc_frame is None:
            if self.validation_form():
                calc = Calc(
                    self.hsp.get_hsp(),
                    get_panel(self.panel.get_selected_panel()),
                    self.specific_data.to_south.value,
                    area=float(self.specific_data.get_value()) if self.specific_data.is_specific_area
                    else None, peak_power_required=float(self.specific_data.get_value())
                    if not self.specific_data.is_specific_area else None)

                self.calc_frame = frame(
                    ft.Column([
                        calc,
                        self.buttons
                    ])
                )

                self.back_button.on_click = self.back

                self.controls[-1] = self.calc_frame
        else:
            if isinstance(self.calc_frame.content.controls[0], Calc):
                self.calc_frame.content.controls[0].continue_button()

        self.update()

    def back(self, e):
        calc = self.calc_frame.content.controls[0]

        if isinstance(calc, Calc):
            if calc.all_calcs.visible:
                self.controls[-1] = self.form_frame
                self.calc_frame = None
            else:
                calc.back_button()


        self.update()
