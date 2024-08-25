import flet as ft

from objects.panel import Panel
from static_object import StaticPanel


class PanelView(ft.View):
    def __init__(self):
        super().__init__()

        self.panel: Panel = StaticPanel().get_panel()

        self.route = '/selected_panel'

        self.appbar = ft.AppBar(
            bgcolor=ft.colors.BLUE_400,
            title=ft.Text(self.panel.id_panel, size=20),
            leading=ft.IconButton(ft.icons.ARROW_LEFT, on_click=lambda e: self.page.go('/'))
        )
