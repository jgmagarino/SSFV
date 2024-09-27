"""
Aqui probare los componentes que voy creando
"""
from components.show_components import *
from src.Mappers.panel_mapper import *
import flet as ft


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    new = get_panel("mejor")

    page.controls.append(ShowPanel(new))
    page.update()

ft.app(main)


