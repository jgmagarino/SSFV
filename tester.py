"""
Aqui probare los componentes que voy creando
"""

import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_dismissal_start(e):
        page.add(ft.Text("Drawer dismissed"))

    def handle_change_start(e):
        page.add(ft.Text(f"Selected Index changed: {e.selected_index}"))
        # page.close(drawer)

    drawer = ft.NavigationDrawer(
        on_dismiss=handle_dismissal_start,
        on_change=handle_change_start,
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Item 1",
                icon=ft.icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.MAIL_OUTLINED),
                label="Item 2",
                selected_icon=ft.icons.MAIL,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.PHONE_OUTLINED),
                label="Item 3",
                selected_icon=ft.icons.PHONE,
            ),
        ],
    )

    page.add(ft.ElevatedButton("Show drawer", on_click=lambda e: page.open(drawer)))

    def handle_dismissal(e):
        page.add(ft.Text("End drawer dismissed"))

    def handle_change(e):
        page.add(ft.Text(f"Selected Index changed: {e.control.selected_index}"))
        # page.close(end_drawer)

    end_drawer = ft.NavigationDrawer(
        position=ft.NavigationDrawerPosition.END,
        on_dismiss=handle_dismissal,
        on_change=handle_change,
        controls=[
            ft.Text("Hola")
        ],
    )

    page.add(ft.ElevatedButton("Show end drawer end", on_click=lambda e: page.open(end_drawer)))

ft.app(main)