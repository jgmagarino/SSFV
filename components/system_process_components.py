import flet as ft


def is_specify_area():
    text = ft.Text("Se tiene un area disponible?")

    button_yes = ft.ElevatedButton("Si")
    button_no = ft.ElevatedButton("No")

    button_row = ft.Row([button_yes, button_no])

    return ft.Container(
        content=ft.Column([
            text,
            button_row
        ]),
        border_radius=10,
        bgcolor=ft.colors.WHITE
    )


def sepecify_area():
    text_field = ft.TextField(label="Area disponible")
    area = ft.Row([text_field, ft.Text("m^2")])

    button_continue = ft.ElevatedButton("Continuar")
    button_back = ft.ElevatedButton("Atras")

    button_row = ft.Row([button_continue, button_back])

    return ft.Container(
        content=ft.Column([
            area,
            button_row
        ])
    )


def util_energy():
    text_field = ft.TextField(label="Potencia a instalar")
    potencia = ft.Row([text_field, ft.Text("W")])

    dropdown = ft.Dropdown(
        label="Zona donde sera el SSFV",
        
    )

    button_continue = ft.ElevatedButton("Continuar")
    button_back = ft.ElevatedButton("Atras")

    button_row = ft.Row([button_continue, button_back])

    return ft.Container(
        content=ft.Column([
            potencia,
            button_row
        ])
    )


def num_panels():
    pass