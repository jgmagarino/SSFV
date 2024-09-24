import flet as ft
from dns.name import empty


# Campos predefinidos para crear nuevas entidades

def text_filed(label: str="", width: int | float = 100):
    return ft.TextField(
        label=label,
        label_style= ft.TextStyle(size=15,
                              color=ft.colors.BLUE_900),
        focused_border_width=3,
        border_color=ft.colors.BLUE_400,
        width=width,
    )

def error_text(message: str="Error"):
    return ft.Text(message, color=ft.colors.RED, size=20, visible=False)

def unit_of_measurement(unit: str):
    return ft.Container(content=ft.Text(unit), border_radius=10,
                        border=ft.border.all(1, ft.colors.GREY), padding=5)

def frame(content):
    return ft.Container(
        content=content,
        border_radius=5,
        padding=10,
        bgcolor=ft.colors.WHITE
    )

def appbar(title: str):
    return ft.AppBar(
        title=ft.Text(title),
        bgcolor=ft.colors.BLUE_400,
        automatically_imply_leading=False
    )

def dropdown(label: str="", options: list[ft.dropdown.Option]=None, width: int | float=250):
    return ft.Dropdown(
        options=options,
        label=label,
        border_color=ft.colors.BLUE_400,
        label_style=ft.TextStyle(color=ft.colors.BLUE_900),
        focused_border_width=3,
        width=width,
    )

def text_and_bg(text: str="", bg: str=ft.colors.BLUE_400):
    return ft.Container(content=ft.Text(value=text), bgcolor=bg,
                        padding=5, border_radius=5)