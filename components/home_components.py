import flet as ft
from objects.json_manager import (load_elements)
from components.tables import (get_hsp, get_tecnologias, get_paneles)


def navigation_rail(height):
    all_sistems = ft.NavigationRailDestination(
        icon=ft.icons.ELECTRIC_METER_OUTLINED,
        selected_icon=ft.icons.ELECTRIC_METER_ROUNDED,
        label="Sistemas"
    )
    all_panels = ft.NavigationRailDestination(
        icon=ft.icons.SOLAR_POWER_OUTLINED,
        selected_icon=ft.icons.SOLAR_POWER_ROUNDED,
        label="Paneles",
        padding=ft.padding.only(top=20)
    )

    all_hsp = ft.NavigationRailDestination(
        icon=ft.icons.WB_SUNNY_OUTLINED,
        selected_icon=ft.icons.SUNNY,
        label="Horas solares pico",
        padding=ft.padding.only(top=20)
    )

    all_technologies = ft.NavigationRailDestination(
        icon=ft.icons.ENERGY_SAVINGS_LEAF_OUTLINED,
        selected_icon=ft.icons.ENERGY_SAVINGS_LEAF_ROUNDED,
        label="Tecnologias",
        padding=ft.padding.only(top=20)
    )

    my_help = ft.NavigationRailDestination(
        icon=ft.icons.HELP_OUTLINE,
        selected_icon=ft.icons.HELP_OUTLINED,
        label="Ayuda",
        padding=ft.padding.only(top=height - 450)
    )

    settings = ft.NavigationRailDestination(
        icon=ft.icons.SETTINGS_OUTLINED,
        selected_icon=ft.icons.SETTINGS_ROUNDED,
        label="Configuracion",
        padding=ft.padding.only(top=20)
    )

    return ft.NavigationRail(
        height=height,
        selected_index=0,
        label_type=ft.NavigationRailLabelType.SELECTED,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        group_alignment=-0.9,
        destinations=[
            all_sistems,
            all_panels,
            all_hsp,
            all_technologies,
            my_help,
            settings
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )


def navigation_drawer():

    all_systems = ft.NavigationDrawerDestination(
        icon=ft.icons.ELECTRIC_METER_OUTLINED,
        selected_icon=ft.icons.ELECTRIC_METER_ROUNDED,
        label="Sistemas"
    )
    all_panels = ft.NavigationDrawerDestination(
        icon=ft.icons.SOLAR_POWER_OUTLINED,
        selected_icon=ft.icons.SOLAR_POWER_ROUNDED,
        label="Paneles",
    )

    all_hsp = ft.NavigationDrawerDestination(
        icon=ft.icons.WB_SUNNY_OUTLINED,
        selected_icon=ft.icons.SUNNY,
        label="Horas solares pico",
    )

    all_technologies = ft.NavigationDrawerDestination(
        icon=ft.icons.ENERGY_SAVINGS_LEAF_OUTLINED,
        selected_icon=ft.icons.ENERGY_SAVINGS_LEAF_ROUNDED,
        label="Tecnologias",
    )

    my_help = ft.NavigationDrawerDestination(
        icon=ft.icons.HELP_OUTLINE,
        selected_icon=ft.icons.HELP_OUTLINED,
        label="Ayuda",
    )

    settings = ft.NavigationDrawerDestination(
        icon=ft.icons.SETTINGS_OUTLINED,
        selected_icon=ft.icons.SETTINGS_ROUNDED,
        label="Configuracion",
    )

    return ft.NavigationDrawer(
        position=ft.NavigationDrawerPosition.END,
        controls=[
            all_systems,
            all_panels,
            all_hsp,
            all_technologies,
            ft.Divider(thickness=2),
            my_help,
            settings
        ],
    )





