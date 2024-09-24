import flet as ft
from components.home_components import (DrawerHome, ActivatorDrawer, AppBarHome, GeneralContent)


class HomeView(ft.View):
    def __init__(self):
        super().__init__()
        self.route = '/'

        # Navegacion
        self.end_drawer = DrawerHome()
        self.end_drawer.on_change = self.on_drawer_change

        # Hasta ahora unicamente para mostrar como titulo la opcion seleccionada
        # en el drawer.
        self.appbar = AppBarHome()
        self.add_button = ft.IconButton(ft.icons.ADD, tooltip="Añadir",
                                        icon_size=40, on_click=lambda e: self.page.go('/create_system'))
        self.appbar.actions.append(self.add_button)

        # Contenido que se mostrara en la pagina
        # Como contenido inicial se mustra los sistemas
        self.content = GeneralContent(0)

        # Para mostrar el navigation drawer
        self.floating_action_button = ActivatorDrawer()
        self.floating_action_button.on_click = lambda e: self.page.open(self.end_drawer)

        # Scroll en toda la pagina
        self.scroll = ft.ScrollMode.ADAPTIVE
        # self.auto_scroll = True

        self.controls.append(self.content)

    def on_drawer_change(self, e):
        """
        En este metodo se ira cambiando el contenido que se mustra en dependencia
        de la opcion seleccionada en en navigation drawer.
        """

        if self.end_drawer.selected_index == 0:
            self.appbar.title = ft.Text("Sistemas", size=30)
            self.content.content = GeneralContent(0)
            self.add_button.on_click = lambda e: self.page.go('/create_system')

        if self.end_drawer.selected_index == 1:
            self.appbar.title = ft.Text("Paneles", size=30)
            self.content.content = GeneralContent(1)
            self.add_button.on_click = lambda e: self.page.go('/create_panel')

        if self.end_drawer.selected_index == 2:
            self.appbar.title = ft.Text("Horas solares pico", size=30)
            self.content.content = GeneralContent(2)
            self.add_button.on_click = lambda e: self.page.go('/create_hsp')

        if self.end_drawer.selected_index == 3:
            self.appbar.title = ft.Text("Tecnologias", size=30)
            self.content.content = GeneralContent(3)
            self.add_button.on_click = lambda e: self.page.go('/create_technology')

        if self.end_drawer.selected_index == 4:
            self.appbar.title = ft.Text("Ayuda", size=30)
            self.content.content = ft.Text("Aun nada")

        if self.end_drawer.selected_index == 5:
            self.appbar.title = ft.Text("Configuracion", size=30)
            self.content.content = ft.Text("Aun nada")

        self.page.close(self.end_drawer)
        self.update()