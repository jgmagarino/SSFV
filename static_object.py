"""
Objetos con los que uso la tecnica Singleton
"""

from flet import Page
from objects.panel import Panel


class StaticPage:
    _instance = None
    _page = None

    def __new__(cls, *args, **kwargs,):
        if not cls._instance:
            cls._instance = super(StaticPage, cls).__new__(cls)
        return cls._instance

    def set_page(self, page: Page):
        self._page = page

    def get_page(self):
        return self._page

class StaticPanel:
    _instance = None
    _panel = None

    def __new__(cls, *args, **kwargs, ):
        if not cls._instance:
            cls._instance = super(StaticPanel, cls).__new__(cls)
        return cls._instance

    def set_panel(self, panel: Panel):
        self._panel = panel

    def get_panel(self) -> Panel:
        if self._panel is not None:
            return self._panel

        print(f"Error: no hay panel seleccionado ...")

class StaticEndDrawer:
    _instance = None
    _drawer = None
    def __new__(cls, *args, **kwargs, ):
        if not cls._instance:
            cls._instance = super(StaticEndDrawer, cls).__new__(cls)
        return cls._instance

    def set_drawer(self, drawer):
        self._drawer = drawer

    def get_drawer(self):
        return self._drawer