"""
Aqui probare los componentes que voy creando
"""
from components.show_components import *
from src.Mappers.hsp_mapper import get_hsp
from src.Mappers.panel_mapper import *
import flet as ft

from src.Mappers.system_mapper import get_system
from src.Mappers.technology_mapper import get_technology
from src.proof.proof import panel


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    panels= []

    # for i in range(10):
    #     panels.append(ShowEntity(HSP(f"hsp {i}", 1)))

    page.controls.append(ShowSystem(get_system("primero")))
    page.update()

ft.app(main)


