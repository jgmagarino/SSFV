import flet as ft

from src.Mappers.panel_mapper import (get_all_panels, get_panel)
from src.Mappers.hsp_mapper import (get_all_hps, get_hsp)

from validation import only_real_numbs
from style import (dropdown, text_and_bg, text_filed)


class SelectPanel(ft.Column):
    def __init__(self):
        """
        Aqui se mostraran todos los paneles y se dara la oportunida de crear uno nuevo de ser
        necesario.
        """
        super().__init__()

        "-----------"
        "PROPIEDADES"
        "-----------"

        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        "-----------"
        "COMPONENTES"
        "-----------"

        self.all_panels = dropdown("Que panel se usara?",
                                   [ft.dropdown.Option(i.panel_id) for i in get_all_panels()])
        self.all_panels.on_change = self.get_details

        self.details = ft.Container(visible=False, padding=5, border_radius=5,
                                    border=ft.border.all(1, ft.colors.GREY))

        "----------"
        "ESTRUCTURA"
        "----------"

        self.controls = [
            self.all_panels,
            ft.TextButton("Ver detalles del panel", disabled=True, on_click=self.details_event),
            ft.Row([self.details], scroll=ft.ScrollMode.ADAPTIVE),
            ft.TextButton("Crear uno nuevo", on_click=lambda e: e.page.go("/create_panel")),
            ft.Divider(height=1)
        ]

    "-------"
    "EVENTOS"
    "-------"

    def details_event(self, e):
        self.details.visible = not self.details.visible

        if self.details.visible:
            self.controls[1].text = "Ocultar detalles"
        else:
            self.controls[1].text = "Ver detalles del panel"

        self.update()

    def get_details(self, e):
        panel = get_panel(self.all_panels.value)

        self.details.content=ft.Column([
            ft.Row([ft.Text("Potencia pico:"), text_and_bg(f"{panel.peak_power} Wp")]),
            ft.Row([ft.Text("Material de las celdas:"), text_and_bg(f"{panel.cell_material}")]),
            ft.Row([ft.Text("Area:"), text_and_bg(f"{panel.area} m²")]),
            ft.Row([ft.Text("Precio:"), text_and_bg(f"{panel.price} cup")]),
            ft.Row([ft.Text("Precio del kwh SEN:"), text_and_bg(f"{panel.price_kwh_sen} cup")]),
        ])

        self.controls[1].disabled = False

        self.update()

    def get_selected_panel(self):
        return self.all_panels.value

    def set_error(self):
        self.all_panels.label_style = ft.TextStyle(color=ft.colors.RED)
        self.all_panels.border_color = ft.colors.RED

    def set_normal(self):
        self.all_panels.label_style = ft.TextStyle(color=ft.colors.BLUE_800)
        self.all_panels.border_color = ft.colors.BLUE


class SelectPlace(ft.Column):
    def __init__(self):
        """
        Aqui se mostraran todos los lugares en los que se tiene registrado una hora solar pico
        y se dara la oportunida de registrar uno nuevo de ser necesario.
        """
        super().__init__()

        "-----------"
        "PROPIEDADES"
        "-----------"

        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        "-----------"
        "COMPONENTES"
        "-----------"

        self.all_places = dropdown("Lugar donde se cosntruira",
                                   [ft.dropdown.Option(i.place) for i in get_all_hps()])
        self.all_places.on_change = self.on_change_dropdown

        self.text = ft.Text("Valor de la hora solar pico : ")

        self.value_hsp = text_and_bg("5.2 h/dia")

        self.crear_button = ft.TextButton("Registrar uno nuevo", on_click=lambda e: self.page.go("/create_hsp"))

        "----------"
        "ESTRUCTURA"
        "----------"

        self.controls = [
            self.all_places,
            ft.Row([self.text, self.value_hsp], alignment=ft.MainAxisAlignment.CENTER),
            self.crear_button,
            ft.Divider(height=1)]

    "-------"
    "EVENTOS"
    "-------"

    def on_change_dropdown(self, e):
        self.controls[1] = ft.Row([self.text,
                                   text_and_bg(f"{get_hsp(self.all_places.value).value} h/dia")],
                                  alignment=ft.MainAxisAlignment.CENTER)
        print(self.get_hsp())
        self.update()

    def get_hsp(self):
        if self.all_places.value is None:
            return get_hsp("Por defecto en Cuba")
        return get_hsp(self.all_places.value)


class SpecificData(ft.Column):
    def __init__(self):
        super().__init__()

        "-----------"
        "PROPIEDADES"
        "-----------"

        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        "-----------"
        "COMPONENTES"
        "-----------"

        self.selected_style = ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.BLUE)
        self.not_selected_style = ft.ButtonStyle(color=ft.colors.BLUE, bgcolor=ft.colors.WHITE)

        self.yes_button = ft.ElevatedButton("Si", on_click=self.change_specific_data,
                                            style=self.selected_style)
        self.no_button = ft.ElevatedButton("No", on_click=self.change_specific_data,
                                           style=self.not_selected_style)

        self.is_specific_area = True

        self.specific_area = text_filed(label="Area disponible:", width=150)
        self.specific_area.on_change=only_real_numbs

        self.specific_Pinst = text_filed(label="Potencia a isntalar:", width=150)
        self.specific_Pinst.on_change=only_real_numbs

        self.text_filed = text_filed(label="Area disponible:", width=150)
        self.text_filed.on_change=only_real_numbs

        self.to_south = ft.Checkbox(label="Orientados al sur")

        "----------"
        "ESTRUCTURA"
        "----------"

        self.yes_or_no = ft.Container(
            content=ft.Column([
                ft.Text("Se tiene un area especifica?"),
                ft.Divider(height=1),
                ft.Row([self.yes_button, self.no_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ], width=250),
            padding=5,
            border_radius=5,
            border=ft.border.all(1, ft.colors.GREY)
        )

        self.controls = [self.yes_or_no, ft.Row([self.text_filed, self.to_south])]

    "-------"
    "EVENTOS"
    "-------"

    def change_specific_data(self, e):

        self.is_specific_area = not self.is_specific_area

        if self.is_specific_area:
            self.yes_button.style = self.selected_style
            self.no_button.style = self.not_selected_style

            self.text_filed.label = "Area disponible:"
        else:
            self.no_button.style = self.selected_style
            self.yes_button.style = self.not_selected_style

            self.text_filed.label = "Potencia a instalar:"

        self.update()


    def get_value(self):
        return self.text_filed.value


    def set_error(self):
        self.text_filed.label_style = ft.TextStyle(color=ft.colors.RED)
        self.text_filed.border_color = ft.colors.RED

        self.update()


    def set_normal(self):
        self.text_filed.label_style = ft.TextStyle(color=ft.colors.RED)
        self.text_filed.border_color = ft.colors.BLUE

        self.update()

