import flet as ft
from estructura import mi_gestor_pickle


def main(page: ft.Page):
    page.title = "Sistema Solar Fotovoltaico"

    column_sistemas = ft.Column()

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        group_alignment=-0.2,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.SOLAR_POWER_OUTLINED, selected_icon=ft.icons.SOLAR_POWER, label="Sistemas"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.POWER_INPUT,
                label="Paneles",
            ),
            ft.NavigationRailDestination(
                padding=ft.padding.only(bottom=200),
                icon=ft.icons.ELECTRICAL_SERVICES_SHARP,
                label="Tecnologias",
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
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(),
                ft.Column([ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    )


ft.app(target=main)
