import flet as ft


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

