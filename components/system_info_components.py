import flet as ft
from objects.system import System


def get_description(text: str):
    return ft.Container(
        content=ft.Column([ft.Text(text)], scroll=ft.ScrollMode.ADAPTIVE),
        border_radius=10,
        border=ft.border.all(1, ft.colors.GREY_200),
        padding=10,
        width=500,
        height=300,
    )


def get_system_info(system: System, page: ft.Page):
    def data_text(text: str):
        return ft.Container(content=ft.Text(text), bgcolor=ft.colors.GREY_300, border_radius=10, padding=5)

    title = ft.Text(system.name, size=30)

    def change_progress(e):
        if system.progress == 0:
            print("0")
            system.progress = 1
            button_progress.text = "En construccion"
            button_progress.bgcolor = ft.colors.GREEN_400
        if system.progress == 1:
            print("1")
            system.progress = 2
            button_progress.text = "Terminado"
            button_progress.bgcolor = ft.colors.BLUE_400
        if system.progress == 2:
            print("2")
            system.progress = 0
            button_progress.text = "En planificación"
            button_progress.bgcolor = ft.colors.RED_400

        page.update()

    button_progress = ft.ElevatedButton("En planificación", bgcolor=ft.colors.RED_400,
                                        tooltip="Cambiar estado", on_click=change_progress)

    title_row = ft.Row([title, button_progress], alignment=ft.MainAxisAlignment.CENTER, width=500)

    area = ft.Row([ft.Text(f"Area: "),
                   data_text(f"{system.area} m²")], wrap=True)
    util_energy = ft.Row([ft.Text(f"Energia util: "),
                          data_text(f"{system.useful_energy} Wh/dia")], wrap=True)
    num_panels = ft.Row([ft.Text(f"Numero de paneles: "),
                         data_text(f"{system.number_of_panels}")], wrap=True)

    column_1 = ft.Column([
        area,
        util_energy,
        num_panels,
    ])

    title_2 = ft.Text("Calculo economico")
    cost = ft.Row([ft.Text(f"Costo del sistema: "),
                   data_text(f"{system.cost} cup")], wrap=True)
    ingr = ft.Row([ft.Text(f"Ingresos: "),
                   data_text(f"{system.income} cup")], wrap=True)
    periodo_recuperacion = ft.Row([ft.Text(f"Periodo de recuperacion: "),
                                   data_text(f"{system.recovery_period} dias")], wrap=True)

    column_2 = ft.Column([
        cost,
        ingr,
        periodo_recuperacion
    ])

    column_3 = ft.Column([
        ft.Text("Descripcion:"),
        get_description("Recuerde que, en el cálculo del número de paneles, el valor tiene que ser"
                        " un número entero, de ahí que se realice el redondeo al valor inmediato "
                        "superior y se adicione 1 al resultado del cálculo. Recuerde que, en el "
                        "cálculo del número de paneles, el valor tiene que ser un número entero, "
                        "de ahí que se realice el redondeo al valor inmediato superior y se "
                        "adicione 1 al resultado del cálculo. Recuerde que, en el cálculo del número de paneles, el "
                        "valor tiene que ser un número entero, de ahí que se realice el redondeo al valor "
                        "inmediato superior y se adicione 1 al resultado del cálculo. Recuerde que, en el cálculo del "
                        "número de paneles, el valor tiene que ser un número entero, de ahí "
                        "que se realice el redondeo al valor "
                        "inmediato superior y se adicione 1 al resultado del cálculo.Recuerde que, en el cálculo del número de paneles, el valor tiene que ser"
                        " un número entero, de ahí que se realice el redondeo al valor inmediato "
                        "superior y se adicione 1 al resultado del cálculo. Recuerde que, en el "
                        "cálculo del número de paneles, el valor tiene que ser un número entero, "
                        "de ahí que se realice el redondeo al valor inmediato superior y se "
                        "adicione 1 al resultado del cálculo. Recuerde que, en el cálculo del número de paneles, el "
                        "valor tiene que ser un número entero, de ahí que se realice el redondeo al valor "
                        "inmediato superior y se adicione 1 al resultado del cálculo. Recuerde que, en el cálculo del "
                        "número de paneles, el valor tiene que ser un número entero, de ahí "
                        "que se realice el redondeo al valor "
                        "inmediato superior y se adicione 1 al resultado del cálculo.Recuerde que, en el cálculo del número de paneles, el valor tiene que ser"
                        " un número entero, de ahí que se realice el redondeo al valor inmediato "
                        "superior y se adicione 1 al resultado del cálculo. Recuerde que, en el "
                        "cálculo del número de paneles, el valor tiene que ser un número entero, "
                        "de ahí que se realice el redondeo al valor inmediato superior y se "
                        "adicione 1 al resultado del cálculo. Recuerde que, en el cálculo del número de paneles, el "
                        "valor tiene que ser un número entero, de ahí que se realice el redondeo al valor "
                        "inmediato superior y se adicione 1 al resultado del cálculo. Recuerde que, en el cálculo del "
                        "número de paneles, el valor tiene que ser un número entero, de ahí "
                        "que se realice el redondeo al valor "
                        "inmediato superior y se adicione 1 al resultado del cálculo.")
    ])

    eliminar = ft.ElevatedButton("Eliminar", bgcolor=ft.colors.RED_400)

    return ft.Container(
        content=ft.Column([
            title_row,
            column_1,
            title_2,
            column_2,
            column_3,
            ft.Row([eliminar], wrap=True),
        ]),
        border=ft.border.all(1, ft.colors.GREY_300),
        padding=20,
        border_radius=10
    )
