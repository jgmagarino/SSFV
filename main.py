import flet as ft

from static_object import StaticPage
from views.home import HomeView
from views.panel_view import PanelView


def main(page: ft.Page):
    StaticPage().set_page(page)

    page.title = "Routes Example"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.window.height = 667
    page.window.width = 375

    def route_change(route):
        page.views.clear()
        page.views.append(
            HomeView()
        )

        if page.route == "/selected_panel":
            page.views.append(
                PanelView()
            )

        # if page.route == "/register":
        #     page.views.append(
        #         RegisterView(page)
        #     )
        page.update()

    def view_pop(view):
        pass

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.update()

ft.app(main)