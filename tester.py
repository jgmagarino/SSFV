"""
Aqui probare los componentes que voy creando
"""

from components.system_info_components import *
from components.system_process_components import *
from objects.system import *


def main(page: ft.Page):
    page.window.maximized = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    sistema = dict_to_sistema(
        get_unic_value("save/Systems.json", "nombre_sistema", "Sistema de prueba"))

    page.scroll = ft.ScrollMode.ADAPTIVE

    page.add(get_system_info(sistema, page))


ft.app(main, view=ft.WEB_BROWSER)
