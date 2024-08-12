import flet as ft
from views.home import HomeView


def main(page: ft.Page):
    page.title = "Routes Example"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.window.height = 667
    page.window.width = 375

    def route_change(route):
        page.views.clear()
        page.views.append(
            HomeView(page)
        )
        # if page.route == "/home":
        #     page.views.append(
        #         HomeView(page)
        #     )
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


ft.app(main, view=ft.WEB_BROWSER)