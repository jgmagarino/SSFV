import flet as ft
from select import select

from components.other_components import (EntityInfo, WhereUsed)
import objects.db_querys as db
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
        self.center_title = False
        self.toolbar_height = 70


"-----------------------------------"
"Objetos de tipo Content y Miniature"
"-----------------------------------"


class GeneralContent(ft.Container):
    def __init__(self, type_entity: int):
        super().__init__()

        # Lista de elementos que se mostraran
        self.miniature_list = None

        self.type_entity = type_entity

        self.all_button = ft.ElevatedButton("todos", on_click=lambda e: self.change_see_option(1))
        self.used_button = ft.ElevatedButton("usados", on_click=lambda e: self.change_see_option(2))
        self.not_used_button = ft.ElevatedButton("sin usar", on_click=lambda e: self.change_see_option(3))

        # Priemero aparece el boton de mostrar todos seleccionado
        # Este puede variar a mostrar los elementos usados en algun sistema o los que no son usados
        self.all_button.bgcolor = ft.colors.BLUE_300
        self.used_button.bgcolor = ft.colors.WHITE54
        self.not_used_button.bgcolor = ft.colors.WHITE54

        # Agrupo en una fila las opciones de visualizacion de los elementos
        self.see_options = ft.Row([self.all_button, self.used_button, self.not_used_button], wrap=True)

        # Mostrar todos los elementos
        # este metodo modifica el valor de miniature list, añadiendole
        # los elementos
        self.get_entities()

        if self.miniature_list:
            self.content = ft.Row(controls=[self.see_options, ft.Divider(height=1)] + self.miniature_list,
                                  wrap=True, spacing=50, alignment=ft.MainAxisAlignment.CENTER)
        else:
            self.content = ft.Text("Aun no hay elementos de este tipo registrados")


    def get_entities(self, get: "str" = "all"):
        """
        Con este metodo se extraen los elementos de este tipo en dependencia del valor de get.
        :param get: 'all' - devuelve todos, 'used' - los que se usan en algun sistema, 'not' - los que no se usan
        """

        if get == "all":
            if self.type_entity == 0:
                self.miniature_list = [GeneralMiniature(i) for i in db.get_all_systems()]

            if self.type_entity == 1:
                self.miniature_list = [GeneralMiniature(i) for i in db.get_all_panels()]

            if self.type_entity == 2:
                self.miniature_list = [GeneralMiniature(i) for i in db.get_all_hsp()]

            if self.type_entity == 3:
                self.miniature_list = [GeneralMiniature(i) for i in db.get_all_technologies()]

        if get == "used":
            if self.type_entity == 1:
                self.miniature_list = [GeneralMiniature(i) for i in db.used_panels()]

            if self.type_entity == 2:
                self.miniature_list = [GeneralMiniature(i) for i in db.used_hsp()]

            if self.type_entity == 3:
                self.miniature_list = [GeneralMiniature(i) for i in db.used_technologies()]

            if not self.miniature_list:
                self.miniature_list = [ft.Text("No se a usado aun ningun elemento en algun sistema")]

        if get == "not":
            if self.type_entity == 1:
                self.miniature_list = [GeneralMiniature(i) for i in db.used_panels(True)]

            if self.type_entity == 2:
                self.miniature_list = [GeneralMiniature(i) for i in db.used_hsp(True)]

            if self.type_entity == 3:
                self.miniature_list = [GeneralMiniature(i) for i in db.used_technologies(True)]

            if not self.miniature_list:
                self.miniature_list = [ft.Text("Todos los elementos se usan en almenos un sistema")]


    def change_see_option(self, selected: int):
        if selected == 1:
            self.all_button.bgcolor = ft.colors.BLUE_300
            self.used_button.bgcolor = ft.colors.WHITE54
            self.not_used_button.bgcolor = ft.colors.WHITE54
            self.get_entities()

        if selected == 2:
            self.all_button.bgcolor = ft.colors.WHITE54
            self.used_button.bgcolor = ft.colors.BLUE_300
            self.not_used_button.bgcolor = ft.colors.WHITE54
            self.get_entities('used')

        if selected == 3:
            self.all_button.bgcolor = ft.colors.WHITE54
            self.used_button.bgcolor = ft.colors.WHITE54
            self.not_used_button.bgcolor = ft.colors.BLUE_300
            self.get_entities('not')

        self.content = ft.Row(controls=[self.see_options, ft.Divider(height=1)] + self.miniature_list,
                              wrap=True, spacing=50, alignment=ft.MainAxisAlignment.CENTER)

        self.all_button.update()
        self.used_button.update()
        self.not_used_button.update()
        self.update()

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
        self.delete_button = ft.FilledButton("eliminar", on_click=self.delete,
                                             style=ft.ButtonStyle(bgcolor=ft.colors.RED_400))

        # Lo que se puede hacer con cada elemento de este tipo
        # Ver detalles y eliminarlo
        self.buttons = ft.Row(
            [
                self.details_button,
                self.delete_button
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

        # Bordes y padding
        self.border = ft.border.all(0.5, ft.colors.GREY)
        self.border_radius = 5
        self.padding = 5

        # ancho
        self.width = 400

        # todo aun falta crear los componentes para mostrar la informacion de los sistemas
        if isinstance(entity, System):
            self.text = entity.name
            self.all_details = [
                ft.Text(self.text),
                self.buttons
            ]

            self.details_button.on_click = lambda e: print("ver detalles")

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
            WhereUsed(self.entity) if not isinstance(entity, Technology) else ft.Text(""),
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


    def delete(self, e):
        # Panel
        if isinstance(self.entity, Panel):
            db.delete_panel(self.entity.id_panel)

        # Hora solar pico
        if isinstance(self.entity, Hsp):
            db.delete_hsp(self.entity.place)

        # Tecnologia
        if isinstance(self.entity, Technology):
            db.delete_technology(self.entity.technology)

        self.visible = False
        self.update()