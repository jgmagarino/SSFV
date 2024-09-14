import flet as ft

from static_object import StaticPage
from views.create_hsp import CreateHsp
from views.create_system import CreateSystem
from views.home import HomeView
from views.create_panel import CreatePanel
from views.create_technology import CreateTechnology
from views.last_instance import HomeInstance


def main(page: ft.Page):
    StaticPage().set_page(page)

    page.title = "Routes Example"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.window.height = 667
    page.window.width = 375

    def route_change(route):
        page.views.clear()
        page.views.append(
            HomeInstance().get_home()
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
        pass

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.update()

ft.app(main)