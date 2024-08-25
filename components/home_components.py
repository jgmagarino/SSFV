import flet as ft

from components.other_components import (EntityInfo, WhereUsed)
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


class GeneralContent(ft.Container):
    def __init__(self, type_entity: int, entity_list: list = None):
        super().__init__()

        if type_entity == 0:
            if  entity_list is None:
                entity_list = DatabaseConnection().get_all_systems()

        if type_entity == 1:
            if  entity_list is None:
                entity_list = DatabaseConnection().get_all_panels()

        if type_entity == 2:
            if  entity_list is None:
                entity_list = DatabaseConnection().get_all_hsp()

        if type_entity == 3:
            if  entity_list is None:
                entity_list = DatabaseConnection().get_all_technologies()

        self.entity_list = [GeneralMiniature(i) for i in entity_list]

        if self.entity_list:
            self.content = ft.Row(controls=self.entity_list, wrap=True, spacing=50)
        else:
            self.content = ft.Text("Aun no hay elementos de este tipo registrados")


class GeneralMiniature(ft.Container):
    def __init__(self, entity: System | Panel | Hsp | Technology):
        """
        Este objeto reprecenta una entidad con la opcion de eliminarla o ver todos sus detalles

        :param entity: entidad a representar
        """
        super().__init__()

        self.entity = entity

        # esta variable indica si se mostraran los detalles de la entidad o no
        self.see = False

        # boton para ver los detalles
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

        # ancho
        self.width = 300

        # todo aun falta crear los componentes para mostrar la informacion de los sistemas
        if isinstance(entity, System):
            self.text = entity.name
            self.all_details = [
                ft.Text(self.text),
                self.buttons
            ]

        # Panel
        if isinstance(entity, Panel):
            self.text = entity.id_panel

        # Hora solar pico
        if isinstance(entity, Hsp):
            self.text = entity.place

        # Tecnologia
        if isinstance(entity, Technology):
            self.text = entity.technology


        self.all_details = [
            ft.Text(self.text),
            EntityInfo(self.entity),
            WhereUsed(self.entity),
            self.buttons
        ]

        # cuerpo de la miniatura
        self.content = ft.Column([ft.Text(self.text), self.buttons],
                                 horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def see_details(self, e):
        """
        Evento para mostrar mas informacion sobre la entidad

        :param e: ni idea
        :return:
        """

        # Ocultar
        if self.see:
            self.content = ft.Column([ft.Text(self.text), self.buttons],
                                     horizontal_alignment=ft.CrossAxisAlignment.CENTER)

            self.details_button.text = "ver detalles"
            self.border = ft.border.all(0.5, ft.colors.GREY)

        # Mostrar
        else:
            self.content = ft.Column(
            controls=self.all_details,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER)

            self.details_button.text = "ocultar"
            self.border = ft.border.all(3, ft.colors.BLUE_600)

        self.see = not self.see
        self.update()