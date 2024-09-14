import flet as ft


class AddPanel(ft.Container):
    def __init__(self):
        super().__init__()

        self.id_panel = ft.Column([ft.TextField(label="Identificador del panel",
                                                border_color=ft.colors.BLUE_400,
                                                label_style=ft.TextStyle(color=ft.colors.BLUE_600),
                                                focused_border_width=3),
                                   ft.Text("Puede ser un numero o un nombre, pero"
                                           " debe ser unico su valor. Ejemplo:"
                                           " Panel 1",
                                           color=ft.colors.GREY_500)
                                   ], spacing=0.1)

        self.cell_material = ft.Column([ft.TextField(label="Identificador del panel",
                                                     border_color=ft.colors.BLUE_400,
                                                     label_style=ft.TextStyle(color=ft.colors.BLUE_600),
                                                     focused_border_width=3),
                                        ft.Text("No es un valor unico",
                                                color=ft.colors.GREY_500)
                                        ], spacing=0.1)

        self.peak_power = ft.Row([ft.TextField(label="Potencia pico", border_color=ft.colors.BLUE_400,
                                               label_style=ft.TextStyle(color=ft.colors.BLUE_600),
                                               focused_border_width=3, width=100),
                                  ft.Container(content=ft.Text("kw"), border_radius=10,
                                               border=ft.border.all(1, ft.colors.GREY), padding=5)])

        self.area = ft.Row([ft.TextField(label="Area", border_color=ft.colors.BLUE_400,
                                         label_style=ft.TextStyle(color=ft.colors.BLUE_600),
                                         focused_border_width=3, width=100),
                            ft.Container(content=ft.Text("m^2"), border_radius=10,
                                         border=ft.border.all(1, ft.colors.GREY), padding=5)])

        self.price = ft.Row([ft.TextField(label="Precio", border_color=ft.colors.BLUE_400,
                                          label_style=ft.TextStyle(color=ft.colors.BLUE_600),
                                          focused_border_width=3, width=100),
                             ft.Container(content=ft.Text("cup"), border_radius=10,
                                          border=ft.border.all(1, ft.colors.GREY), padding=5)])

        self.price_kwh_sen = ft.Row([ft.TextField(label="Precio del Kwh SEN", border_color=ft.colors.BLUE_400,
                                                  label_style=ft.TextStyle(color=ft.colors.BLUE_600),
                                                  focused_border_width=3, width=100),
                                     ft.Container(content=ft.Text("cup"), border_radius=10,
                                                  border=ft.border.all(1, ft.colors.GREY), padding=5)])

        self.create = ft.ElevatedButton("Crear", bgcolor=ft.colors.BLUE_400, color=ft.colors.WHITE)
        self.cancelate = ft.ElevatedButton("Cancelar")

        self.border = ft.border.all(1, ft.colors.GREY),
        self.border_radius = 5,
        self.padding = 10

        self.content = ft.Row([
                    self.id_panel,
                    self.cell_material,
                    ft.Row([self.peak_power,
                    self.area], spacing=30, alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([self.price,
                            self.price_kwh_sen], spacing=30, alignment=ft.MainAxisAlignment.CENTER),
                    ft.Divider(height=1),
                    ft.Row([self.create, self.cancelate], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ], wrap=True
                )