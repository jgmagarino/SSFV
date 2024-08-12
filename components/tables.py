import flet as ft


def add_cells(data: list, table: ft.DataTable):
    for p in data:

        new_row = ft.DataRow(cells=[])

        for key, value in p.items():
            new_row.cells.append(ft.DataCell(ft.Text(f"{value}")))

        table.rows.append(new_row)


def get_paneles(data: list):
    table_panel = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Id")),
            ft.DataColumn(ft.Text("Potencia pico")),
            ft.DataColumn(ft.Text("Material de las celdas")),
            ft.DataColumn(ft.Text("Area")),
            ft.DataColumn(ft.Text("Precio")),
            ft.DataColumn(ft.Text("Precio kwh SEN"))
        ],
        column_spacing=30
    )

    #  table_panel.vertical_lines = ft.BorderSide(0.4)

    table_panel.divider_thickness = 1

    add_cells(data, table_panel)

    horizontal_scroll = ft.Row([table_panel], scroll=ft.ScrollMode.ADAPTIVE)

    return ft.Container(
        content=ft.Column([horizontal_scroll],
                          scroll=ft.ScrollMode.ADAPTIVE, alignment=ft.alignment.top_center),

        bgcolor=ft.colors.BLACK26,
        width=500, height=500,
        padding=10,
        border_radius=10,
        alignment=ft.alignment.top_center
    )


def get_hsp(data: list):
    table_hsp = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Zona")),
            ft.DataColumn(ft.Text("Valor")),
        ],
        column_spacing=30
    )

    add_cells(data, table_hsp)

    horizontal_scroll = ft.Row([table_hsp], scroll=ft.ScrollMode.ADAPTIVE)

    return ft.Container(
        content=ft.Column([horizontal_scroll],
                          scroll=ft.ScrollMode.ADAPTIVE, alignment=ft.alignment.top_center),

        bgcolor=ft.colors.BLACK26,
        width=200, height=500,
        padding=10,
        border_radius=10,
        alignment=ft.alignment.top_center
    )


def get_tecnologias(data: list):
    table_tecnologias = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Material")),
            ft.DataColumn(ft.Text("Area")),
        ],
        column_spacing=30
    )

    add_cells(data, table_tecnologias)

    horizontal_scroll = ft.Row([table_tecnologias], scroll=ft.ScrollMode.ADAPTIVE)

    return ft.Container(
        content=ft.Column([horizontal_scroll],
                          scroll=ft.ScrollMode.ADAPTIVE, alignment=ft.alignment.top_center),

        bgcolor=ft.colors.BLACK26,
        width=200, height=500,
        padding=10,
        border_radius=10,
        alignment=ft.alignment.top_center
    )
