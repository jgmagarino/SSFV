import flet as ft
from organizacion import arry_columns

global column


def main(page: ft.Page):
    page.title = "Sistema Solar Fotovoltaico"

    global column
    column = arry_columns[0]

    def change_column(e):
        global column
        column = arry_columns[e.control.selected_index]

        row.controls.pop()
        row.controls.append(column)

        page.update()

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        group_alignment=-0.2,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.SOLAR_POWER_OUTLINED,
                selected_icon=ft.icons.SOLAR_POWER,
                label="Sistemas"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.POWER_INPUT,
                label="Paneles",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.ELECTRICAL_SERVICES_SHARP,
                label="Tecnologias",
            ),
            ft.NavigationRailDestination(
                padding=ft.padding.only(bottom=200),
                icon=ft.icons.SUNNY,
                label="HSP",
            ),
            ft.NavigationRailDestination(
                padding=ft.padding.only(top=100),
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon=ft.icons.SETTINGS,
                label="Configuracion"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.HELP_OUTLINE,
                selected_icon=ft.icons.HELP,
                label="Ayuda"
            )
        ],
        on_change=change_column,
    )

    row = ft.Row(
            [
                rail,
                ft.VerticalDivider(),
                column,
            ],
            expand=True,
        )

    page.add(row)


ft.app(target=main)
