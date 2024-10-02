import flet as ft

from views.create_hsp import CreateHsp
from views.create_panel import CreatePanel
from views.create_system import CreateSystem
from views.create_technology import CreateTechnology
from views.home import HomeView
from views.system_view import SystemView


def main(page: ft.Page):

    page.title = "SSFV"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.window.height = 667
    page.window.width = 375

    def route_change(route):

        if page.route == '/':
            page.views.clear()
            page.views.append(
                HomeView()
            )

        if page.route == 'back':
            page.views.pop()


        if page.route == '/system_view':
            page.views.append(
                SystemView()
            )

        if page.route == "/create_system":
            page.views.append(
                CreateSystem()
            )

        if page.route == "/create_panel":
            page.views.append(
                CreatePanel()
            )

        if page.route == "/create_hsp":
            page.views.append(
                CreateHsp()
            )

        if page.route == "/create_technology":
            page.views.append(
                CreateTechnology()
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        page.go(page.views[-1].route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.update()

ft.app(main)