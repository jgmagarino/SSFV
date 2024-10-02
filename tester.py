"""
Aqui probare los componentes que voy creando
"""
from components.show_components import *
from src.Mappers.hsp_mapper import get_hsp
from src.Mappers.panel_mapper import *
import flet as ft

from components.system_calc import *


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    panel = Panel("Panel de prueba", 450, "Silicio monocristalino", 2.1,
                  30000, 30)

    page.scroll = ft.ScrollMode.ADAPTIVE

    page.controls.append(Calc(get_hsp("Por defecto en Cuba"), get_panel("Hiku"),
                              False, peak_power_required=16920))
    page.update()

ft.app(main)


