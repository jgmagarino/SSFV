import flet as ft
from objetos.json_manager import load_elements
from components.tables import (get_hsp, get_tecnologias, get_paneles)
from components.home_components import (navigation_drawer)


class HomeView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.drawer = navigation_drawer()
        self.drawer.on_change = self.on_change

        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.appbar = ft.AppBar(automatically_imply_leading=False, title=ft.Text("Sistemas"))

        self.floating_action_button = ft.FloatingActionButton(icon=ft.icons.MENU,
                                                              on_click=lambda e: page.open(self.drawer))
        self.floating_action_button_location = ft.FloatingActionButtonLocation.END_FLOAT

        self.scroll = ft.ScrollMode.ADAPTIVE
        self.bgcolor = ft.colors.BLUE_200

    def on_change(self, e):

        no_elements = ft.Text("No hay elementos de este tipo...")

        if len(self.controls) != 0:
            self.controls.pop()

        if e.control.selected_index == 0:
            aux = load_elements("salva/Sistemas.json")
            self.appbar.title = ft.Text("Sistemas")
            if len(aux) != 0:
                self.controls.append(get_paneles(aux))
            else:
                self.controls.append(no_elements)

        if e.control.selected_index == 1:
            aux = load_elements("salva/Paneles.json")
            self.appbar.title = ft.Text("Paneles")
            if len(aux) != 0:
                self.controls.append(get_paneles(aux))
            else:
                self.controls.append(no_elements)

        if e.control.selected_index == 2:
            aux = load_elements("salva/Hsp.json")
            self.appbar.title = ft.Text("Horas Solares Pico")
            if len(aux) != 0:
                self.controls.append(get_hsp(aux))
            else:
                self.controls.append(no_elements)

        if e.control.selected_index == 3:
            aux = load_elements("salva/Tecnologias.json")
            self.appbar.title = ft.Text("Tecnologias")
            if len(aux) != 0:
                self.controls.append(get_tecnologias(aux))
            else:
                self.controls.append(no_elements)

        self.drawer.open = False
        self.update()
