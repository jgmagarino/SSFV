import flet as ft
from flet_core.colors import BLUE_50

from components.other_components import (EntityInfo, WhereUsed)
from src.Mappers.system_mapper import get_all_systems
from src.modules.system_module import System
from src.modules.technology_module import Technology
from src.modules.panel_module import Panel
from src.modules.hsp_module import HSP
from src.Mappers.hsp_mapper import (get_all_hps)
from src.Mappers.panel_mapper import (get_all_panels)
from src.Mappers.technology_mapper import (get_all_technologies)


class DrawerHome(ft.NavigationDrawer):
    def __init__(self):
        super().__init__()

        self.position = ft.NavigationDrawerPosition.END
        self.indicator_color = ft.colors.BLUE_100

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
            ft.Divider(height=1),
            ft.NavigationDrawerDestination(
                icon_content=ft.Row([ft.Icon(name=ft.icons.DELETE_OUTLINE, color=ft.colors.RED),
                                     ft.Text("Papelera", color=ft.colors.RED)]),
                selected_icon_content=ft.Row([ft.Icon(name=ft.icons.DELETE, color=ft.colors.RED),
                                     ft.Text("Papelera", color=ft.colors.RED)]),
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

        self.type_entity = type_entity

        "-----------"
        "COMPONENTES"
        "-----------"

        self.selected_style = ft.ButtonStyle(bgcolor=ft.colors.BLUE, color=ft.colors.WHITE)
        self.not_selected_style = ft.ButtonStyle(bgcolor=ft.colors.GREY, color=ft.colors.BLACK)

        # Lista de elementos que se mostraran
        self.miniature_list = None

        self.all_button = ft.ElevatedButton("todos", on_click=lambda e: self.change_see_option(1))
        self.used_button = ft.ElevatedButton("usados", on_click=lambda e: self.change_see_option(2))
        self.not_used_button = ft.ElevatedButton("sin usar", on_click=lambda e: self.change_see_option(3))

        # Priemero aparece el boton de mostrar todos seleccionado
        # Este puede variar a mostrar los elementos usados en algun sistema o los que no son usados
        self.all_button.style = self.selected_style
        self.used_button.style = self.not_selected_style
        self.not_used_button.style = self.not_selected_style

        "----------"
        "ESTRUCTURA"
        "----------"

        # Agrupo en una fila las opciones de visualizacion de los elementos
        self.see_options = ft.Row([self.all_button, self.used_button, self.not_used_button], wrap=True)

        # Mostrar todos los elementos
        # este metodo modifica el valor de miniature list, añadiendole
        # los elementos
        self.get_entities()

        if self.miniature_list:
            self.content = ft.Column(controls=[self.see_options, ft.Divider(height=1)] + self.miniature_list)
        else:
            self.content = ft.Text("Aun no hay elementos de este tipo registrados")


    def get_entities(self, get: "str" = "all"):
        """
        Con este metodo se extraen los elementos de este tipo en dependencia del valor de get.
        :param get: 'all' - devuelve todos, 'used' - los que se usan en algun sistema, 'not' - los que no se usan
        """

        if get == "all":
            if self.type_entity == 0:
                self.miniature_list = [GeneralMiniature(i) for i in get_all_systems() if i.visible == 1]

            if self.type_entity == 1:
                self.miniature_list = [GeneralMiniature(i) for i in get_all_panels() if i.visible == 1]

            if self.type_entity == 2:
                self.miniature_list = [GeneralMiniature(i) for i in get_all_hps() if i.visible == 1]

            if self.type_entity == 3:
                self.miniature_list = [GeneralMiniature(i) for i in get_all_technologies() if i.visible == 1]

        if get == "used":
            # todo Cambiar para que solo muestre los que estan usados
            if self.type_entity == 1:
                self.miniature_list = [GeneralMiniature(i) for i in get_all_panels() if i.visible == 1]

            if self.type_entity == 2:
                self.miniature_list = [GeneralMiniature(i) for i in get_all_hps() if i.visible == 1]

            if self.type_entity == 3:
                self.miniature_list = [GeneralMiniature(i) for i in get_all_technologies() if i.visible == 1]

            if not self.miniature_list:
                self.miniature_list = [ft.Text("No se a usado aun ningun elemento en algun sistema")]

        if get == "not":
            # todo Cambiar para que solo muestre los que no estan usados
            if self.type_entity == 1:
                self.miniature_list = [GeneralMiniature(i) for i in get_all_panels() if i.visible == 1]

            if self.type_entity == 2:
                self.miniature_list = [GeneralMiniature(i) for i in get_all_hps() if i.visible == 1]

            if self.type_entity == 3:
                self.miniature_list = [GeneralMiniature(i) for i in get_all_technologies() if i.visible == 1]

            if not self.miniature_list:
                self.miniature_list = [ft.Text("Todos los elementos se usan en almenos un sistema")]


    def change_see_option(self, selected: int):
        if selected == 1:
            self.all_button.style = self.selected_style
            self.used_button.style = self.not_selected_style
            self.not_used_button.style = self.not_selected_style
            self.get_entities()

        if selected == 2:
            self.all_button.style = self.not_selected_style
            self.used_button.style = self.selected_style
            self.not_used_button.style = self.not_selected_style
            self.get_entities('used')

        if selected == 3:
            self.all_button.style = self.not_selected_style
            self.used_button.style = self.not_selected_style
            self.not_used_button.style = self.selected_style
            self.get_entities('not')

        self.content = ft.Column(controls=[self.see_options, ft.Divider(height=1)] + self.miniature_list)

        self.update()


class GeneralMiniature(ft.Container):
    def __init__(self, entity: System | Panel | HSP | Technology):
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
            self.text = entity.panel_id

        # Hora solar pico
        if isinstance(entity, HSP):
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

        self.entity.visible = 0
        # todo hace falta un metodo para actualizar el estado de la entidad
        self.visible = False
        self.update()