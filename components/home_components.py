import flet as ft

from components.other_components import (PanelInfo, PanelOnSystem, HspInfo, HspOnSystem,
                                         TechnologyOnSystem, TechnologyInfo)
from db_gestor import DatabaseConnection
from objects.hsp import Hsp
from objects.panel import Panel
from objects.system import System
from objects.technology import Technology


class DrawerHome(ft.NavigationDrawer):
    def __init__(self):
        super().__init__()

        self.position = ft.NavigationDrawerPosition.END

        self.controls = [
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Sistemas",
                icon=ft.icons.BRIGHTNESS_7_OUTLINED,
                selected_icon=ft.icons.BRIGHTNESS_7,
            ),
            ft.NavigationDrawerDestination(
                label="Paneles",
                icon=ft.icons.SOLAR_POWER_OUTLINED,
                selected_icon=ft.icons.SOLAR_POWER,
            ),
            ft.NavigationDrawerDestination(
                label="Horas solares pico",
                icon=ft.icons.ACCESS_TIME_OUTLINED,
                selected_icon=ft.icons.ACCESS_TIME_FILLED,
            ),
            ft.NavigationDrawerDestination(
                label="Tecnologias",
                icon=ft.icons.DEVICES,
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon=ft.icons.MAIL_OUTLINED,
                label="Ayuda",
                selected_icon=ft.icons.MAIL,
            ),
            ft.NavigationDrawerDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                label="Configuracion",
                selected_icon=ft.icons.SETTINGS_ROUNDED,
            ),
        ]


class ActivatorDrawer(ft.FloatingActionButton):
    def __init__(self):
        super().__init__()
        self.bgcolor = ft.colors.BLUE_300
        self.icon = ft.icons.ARROW_LEFT


class AppBarHome(ft.AppBar):
    def __init__(self):
        super().__init__()
        self.title = ft.Text("Sistemas", size=30)
        self.automatically_imply_leading = False
        self.bgcolor = ft.colors.BLUE_400
        self.actions = [ft.Container(height=0, width=0)]
        self.center_title = True


"-----------------------------------"
"Objetos de tipo Content y Miniature"
"-----------------------------------"


class ContentSystem(ft.Container):
    """
    Este objeto contiene la lista de todos los elementos de
    su entidad en forma de Miniature"entidad".
    """

    def __init__(self):
        super().__init__()

        # Carga todos los elementos de la BD los convierte en Miniature"entidad"
        # y los guarda en una lista.
        systems = [MiniatureSystem(i) for i in DatabaseConnection().get_all_systems()]

        if systems:
            self.content = ft.Row(controls=systems, wrap=True)
        else:
            self.content = ft.Text("Aun no se han creado sistemas")


class MiniatureSystem(ft.Container):
    """
    Este objeto sirve para reprecentar todas las entidades en una lista.
    dando la posibilidad de ver el identificador de la entidad, ver mas
    detalles o eliminarlas.
    """

    def __init__(self, system: System):
        super().__init__()

        self.system = system

        # Lo que se puede hacer con cada elemento de este tipo
        # Ver detalles y eliminarlo
        self.buttons = ft.Row(
            [
                ft.ElevatedButton("ver detalles"),
                ft.FilledButton("eliminar", style=ft.ButtonStyle(bgcolor=ft.colors.RED_400))
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

        # Bordes y padding
        self.border = ft.border.all(0.5, ft.colors.GREY)
        self.border_radius = 5
        self.padding = 5

        # Cuerpo de la miniatura
        self.body = ft.Column([ft.Text(self.system.name), self.buttons],
                              horizontal_alignment=ft.CrossAxisAlignment.CENTER)


class ContentPanels(ft.Container):
    """
    Este objeto contiene la lista de todos los elementos de
    su entidad en forma de Miniature"entidad".
    """

    def __init__(self, panels: list[Panel] = None):
        """
        :param panels: lista de paneles que se quieren mostrar, pueden ser todos o unos especificados.
        """
        super().__init__()

        # Si no entran ningun panel como parametro, se cargan todos
        if panels is None:
            panels = DatabaseConnection().get_all_panels()

        # Convierte los paneles en Miniature"entidad"
        # y los guarda en una lista.
        self.panels = [MiniaturePanel(i) for i in panels]

        if panels:
            self.content = ft.Row(controls=self.panels, wrap=True, spacing=50)
        else:
            self.content = ft.Text("No hay paneles registrados")


class MiniaturePanel(ft.Container):
    """
    Este objeto sirve para reprecentar todas las entidades en una lista.
    dando la posibilidad de ver el identificador de la entidad, ver mas
    detalles o eliminarlas.
    """

    def __init__(self, panel: Panel):
        super().__init__()

        self.panel = panel

        # def see_details(e):
        #     StaticPanel().set_panel(self.panel)
        #     StaticPage().get_page().go('/selected_panel')

        self.see = False

        self.details_button = ft.ElevatedButton("ver detalles", on_click=self.see_details)

        # Lo que se puede hacer con cada elemento de este tipo
        # Ver detalles y eliminarlo
        self.buttons = ft.Row(
            [
                self.details_button,
                ft.FilledButton("eliminar", style=ft.ButtonStyle(bgcolor=ft.colors.RED_400))
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

        # Bordes y padding
        self.border = ft.border.all(0.5, ft.colors.GREY)
        self.border_radius = 5
        self.padding = 5

        self.width = 300

        # cuerpo de la miniatura
        self.content = ft.Column([ft.Text(self.panel.id_panel), self.buttons],
                              horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def see_details(self, e):
        if self.see:
            self.content = ft.Column([ft.Text(self.panel.id_panel), self.buttons],
                                     horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            self.details_button.text = "ver detalles"
            self.border = ft.border.all(0.5, ft.colors.GREY)

        else:
            self.content = ft.Column(
            [
                ft.Text(self.panel.id_panel),
                PanelInfo(self.panel),
                PanelOnSystem(self.panel),
                self.buttons,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            self.details_button.text = "ocultar"
            self.border = ft.border.all(3, ft.colors.BLUE_600)

        self.see = not self.see
        self.update()


class ContentHsp(ft.Container):
    """
    Este objeto contiene la lista de todos los elementos de
    su entidad en forma de Miniature"entidad".
    """

    def __init__(self, hsp: list[Hsp] = None):
        """
        :param hsp: lista de hsp que se quieren mostrar, pueden ser todos o unos especificados.
        """
        super().__init__()

        # Si no entran ningun panel como parametro, se cargan todos
        if hsp is None:
            hsp = DatabaseConnection().get_all_hsp()

        # Convierte los paneles en Miniature"entidad"
        # y los guarda en una lista.
        self.hsp = [MiniatureHsp(i) for i in hsp]

        if hsp:
            self.content = ft.Row(controls=self.hsp, wrap=True, spacing=50)
        else:
            self.content = ft.Text("No hay lugares registrados")


class MiniatureHsp(ft.Container):
    """
    Este objeto sirve para reprecentar todas las entidades en una lista.
    dando la posibilidad de ver el identificador de la entidad, ver mas
    detalles o eliminarlas.
    """

    def __init__(self, hsp: Hsp):
        super().__init__()

        self.hsp = hsp

        # def see_details(e):
        #     StaticPanel().set_panel(self.panel)
        #     StaticPage().get_page().go('/selected_panel')

        self.see = False

        self.details_button = ft.ElevatedButton("ver detalles", on_click=self.see_details)

        # Lo que se puede hacer con cada elemento de este tipo
        # Ver detalles y eliminarlo
        self.buttons = ft.Row(
            [
                self.details_button,
                ft.FilledButton("eliminar", style=ft.ButtonStyle(bgcolor=ft.colors.RED_400))
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

        # Bordes y padding
        self.border = ft.border.all(0.5, ft.colors.GREY)
        self.border_radius = 5
        self.padding = 5

        self.width = 300

        # cuerpo de la miniatura
        self.content = ft.Column([ft.Text(self.hsp.place), self.buttons],
                              horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def see_details(self, e):
        if self.see:
            self.content = ft.Column([ft.Text(self.hsp.place), self.buttons],
                                     horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            self.details_button.text = "ver detalles"
            self.border = ft.border.all(0.5, ft.colors.GREY)

        else:
            self.content = ft.Column(
            [
                ft.Text(self.hsp.place),
                HspInfo(self.hsp),
                HspOnSystem(self.hsp),
                self.buttons,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            self.details_button.text = "ocultar"
            self.border = ft.border.all(3, ft.colors.BLUE_600)

        self.see = not self.see
        self.update()


class ContentTechnologies(ft.Container):
    """
    Este objeto contiene la lista de todos los elementos de
    su entidad en forma de Miniature"entidad".
    """

    def __init__(self, technologies: list[Technology] = None):
        """
        :param technologies: lista de tecnologias que se quieren mostrar, pueden ser todos o unos especificados.
        """
        super().__init__()

        # Si no entran ningun panel como parametro, se cargan todos
        if technologies is None:
            technologies = DatabaseConnection().get_all_technologies()

        # Convierte los paneles en Miniature"entidad"
        # y los guarda en una lista.
        self.technologies = [MiniatureTechnology(i) for i in technologies]

        if technologies:
            self.content = ft.Row(controls=self.technologies, wrap=True, spacing=50)
        else:
            self.content = ft.Text("No hay lugares registrados")

class MiniatureTechnology(ft.Container):
    """
    Este objeto sirve para reprecentar todas las entidades en una lista.
    dando la posibilidad de ver el identificador de la entidad, ver mas
    detalles o eliminarlas.
    """

    def __init__(self, technology: Technology):
        super().__init__()

        self.technology = technology

        # def see_details(e):
        #     StaticPanel().set_panel(self.panel)
        #     StaticPage().get_page().go('/selected_panel')

        self.see = False

        self.details_button = ft.ElevatedButton("ver detalles", on_click=self.see_details)

        # Lo que se puede hacer con cada elemento de este tipo
        # Ver detalles y eliminarlo
        self.buttons = ft.Row(
            [
                self.details_button,
                ft.FilledButton("eliminar", style=ft.ButtonStyle(bgcolor=ft.colors.RED_400))
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

        # Bordes y padding
        self.border = ft.border.all(0.5, ft.colors.GREY)
        self.border_radius = 5
        self.padding = 5

        self.width = 300

        # cuerpo de la miniatura
        self.content = ft.Column([ft.Text(self.technology.technology), self.buttons],
                                 horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def see_details(self, e):
        if self.see:
            self.content = ft.Column([ft.Text(self.technology.technology), self.buttons],
                                     horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            self.details_button.text = "ver detalles"
            self.border = ft.border.all(0.5, ft.colors.GREY)

        else:
            self.content = ft.Column(
            [
                ft.Text(self.technology.technology),
                TechnologyInfo(self.technology),
                TechnologyOnSystem(self.technology),
                self.buttons,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            self.details_button.text = "ocultar"
            self.border = ft.border.all(3, ft.colors.BLUE_600)

        self.see = not self.see
        self.update()