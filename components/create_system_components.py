import flet as ft

from src.Mappers.panel_mapper import (get_all_panels, get_panel)
from src.Mappers.hsp_mapper import (get_all_hps, get_hsp)
from src.Mappers.technology_mapper import (get_technology)
from src.modules.panel_module import Panel
from validation import only_real_numbs
from style import (dropdown, text_and_bg, text_filed)


class SelectPanel(ft.Column):
    def __init__(self):
        """
        Aqui se mostraran todos los paneles y se dara la oportunida de crear uno nuevo de ser
        necesario.
        """
        super().__init__()

        "-----------"
        "PROPIEDADES"
        "-----------"

        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        "-----------"
        "COMPONENTES"
        "-----------"

        self.all_panels = dropdown("Que panel se usara?",
                                   [ft.dropdown.Option(i.panel_id) for i in get_all_panels()])
        self.all_panels.on_change = self.get_details

        self.details = ft.Container(visible=False, padding=5, border_radius=5,
                                    border=ft.border.all(1, ft.colors.GREY))

        "----------"
        "ESTRUCTURA"
        "----------"

        self.controls = [
            self.all_panels,
            ft.TextButton("Ver detalles del panel", disabled=True, on_click=self.details_event),
            ft.Row([self.details], scroll=ft.ScrollMode.ADAPTIVE),
            ft.TextButton("Crear uno nuevo", on_click=lambda e: e.page.go("/create_panel")),
            ft.Divider(height=1)
        ]

    "-------"
    "EVENTOS"
    "-------"

    def details_event(self, e):
        self.details.visible = not self.details.visible

        if self.details.visible:
            self.controls[1].text = "Ocultar detalles"
        else:
            self.controls[1].text = "Ver detalles del panel"

        self.update()

    def get_details(self, e):
        panel = get_panel(self.all_panels.value)

        self.details.content=ft.Column([
            ft.Row([ft.Text("Potencia pico:"), text_and_bg(f"{panel.peak_power} Wp")]),
            ft.Row([ft.Text("Material de las celdas:"), text_and_bg(f"{panel.cell_material}")]),
            ft.Row([ft.Text("Area:"), text_and_bg(f"{panel.area} m²")]),
            ft.Row([ft.Text("Precio:"), text_and_bg(f"{panel.price} cup")]),
            ft.Row([ft.Text("Precio del kwh SEN:"), text_and_bg(f"{panel.price_kwh_sen} cup")]),
        ])

        self.controls[1].disabled = False

        self.update()

    def get_selected_panel(self):
        return self.all_panels.value

    def set_error(self):
        self.all_panels.label_style = ft.TextStyle(color=ft.colors.RED)
        self.all_panels.border_color = ft.colors.RED

    def set_normal(self):
        self.all_panels.label_style = ft.TextStyle(color=ft.colors.BLUE_800)
        self.all_panels.border_color = ft.colors.BLUE


class SelectPlace(ft.Column):
    def __init__(self):
        """
        Aqui se mostraran todos los lugares en los que se tiene registrado una hora solar pico
        y se dara la oportunida de registrar uno nuevo de ser necesario.
        """
        super().__init__()

        "-----------"
        "PROPIEDADES"
        "-----------"

        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        "-----------"
        "COMPONENTES"
        "-----------"

        self.all_places = dropdown("Lugar donde se cosntruira",
                                   [ft.dropdown.Option(i.place) for i in get_all_hps()])
        self.all_places.on_change = self.on_change_dropdown

        self.text = ft.Text("Valor de la hora solar pico : ")

        self.value_hsp = text_and_bg("5.2 h/dia")

        self.crear_button = ft.TextButton("Registrar uno nuevo", on_click=lambda e: self.page.go("/create_hsp"))

        "----------"
        "ESTRUCTURA"
        "----------"

        self.controls = [
            self.all_places,
            ft.Row([self.text, self.value_hsp], alignment=ft.MainAxisAlignment.CENTER),
            self.crear_button,
            ft.Divider(height=1)]

    "-------"
    "EVENTOS"
    "-------"

    def on_change_dropdown(self, e):
        self.value_hsp.content.value = f"{get_hsp(self.all_places.value).value} h/dia"
        self.update()

    def get_hsp(self):
        if self.all_places.value is None:
            return 5.2
        return get_hsp(self.all_places.value).value


class SpecificData(ft.Column):
    def __init__(self):
        super().__init__()

        "-----------"
        "PROPIEDADES"
        "-----------"

        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        "-----------"
        "COMPONENTES"
        "-----------"

        self.selected_style = ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.BLUE)
        self.not_selected_style = ft.ButtonStyle(color=ft.colors.BLUE, bgcolor=ft.colors.WHITE)

        self.yes_button = ft.ElevatedButton("Si", on_click=self.change_specific_data,
                                            style=self.selected_style)
        self.no_button = ft.ElevatedButton("No", on_click=self.change_specific_data,
                                           style=self.not_selected_style)

        self.is_specific_area = True

        self.specific_area = text_filed(label="Area disponible:", width=150)
        self.specific_area.on_change=only_real_numbs

        self.specific_Pinst = text_filed(label="Potencia a isntalar:", width=150)
        self.specific_Pinst.on_change=only_real_numbs

        self.text_filed = text_filed(label="Area disponible:", width=150)
        self.text_filed.on_change=only_real_numbs

        self.to_south = ft.Checkbox(label="Orientados al sur")

        "----------"
        "ESTRUCTURA"
        "----------"

        self.yes_or_no = ft.Container(
            content=ft.Column([
                ft.Text("Se tiene un area especifica?"),
                ft.Divider(height=1),
                ft.Row([self.yes_button, self.no_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ], width=250),
            padding=5,
            border_radius=5,
            border=ft.border.all(1, ft.colors.GREY)
        )

        self.controls = [self.yes_or_no, ft.Row([self.text_filed, self.to_south])]

    "-------"
    "EVENTOS"
    "-------"

    def change_specific_data(self, e):

        self.is_specific_area = not self.is_specific_area

        if self.is_specific_area:
            self.yes_button.style = self.selected_style
            self.no_button.style = self.not_selected_style

            self.text_filed.label = "Area disponible:"
        else:
            self.no_button.style = self.selected_style
            self.yes_button.style = self.not_selected_style

            self.text_filed.label = "Potencia a instalar:"

        self.update()


    def get_value(self) -> float:

        value = self.text_filed.value

        return float(value)


class Result(ft.Container):
    def __init__(self, title, details):
        """
        Sirve para mostrar un calculo en especifico y sus detalles que son : Datos, calculo paso a paso
        y resultado.
        :param title: resultado obtenido
        :param details: Datos, calculo paso a paso y resultado.
        """
        super().__init__()

        "-----------"
        "PROPIEDADES"
        "-----------"

        self.border = ft.border.all(1, ft.colors.GREY)
        self.border_radius = 5
        self.padding = 10

        "-----------"
        "COMPONENTES"
        "-----------"

        self.button_details = ft.IconButton(ft.icons.ARROW_UPWARD, on_click=self.close_details)
        self.details = ft.Column([ft.Text(details), self.button_details], visible=False)

        "----------"
        "ESTRUCTURA"
        "----------"

        self.content = ft.Column([
            ft.Row([ft.ElevatedButton(text=title,on_click=self.see_details)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, wrap=True),
            self.details
        ])

    "-------"
    "EVENTOS"
    "-------"

    def close_details(self, e):
        self.details.visible = False

        self.update()

    def see_details(self, e):
        self.details.visible = not self.details.visible

        self.update()


class CalcWithArea(ft.Column):
    def __init__(self, area: float, id_panel: str, place: float, to_south: bool):
        """
        Aqui realizo todos los calculos teniendo un area especificada, para cada  calculo existe
        'variable_value' que guarda el resultado del calculo y 'variable', que guarda la descripcion
        del calculo.

        :param area: area especificada
        :param id_panel: panel que se usara
        :param place: lugar donde se construira
        :param to_south: si los paneles estan orientados al sur o no
        """
        super().__init__()

        technology = get_technology(get_panel(id_panel).cell_material).get_min_surface_req()

        self.approx_peak_power_value = round(area / technology, 2)
        self.approx_peak_power = (
            "Se realiza un calculo aproximado segun la tecnologia del panel para obtener "
            "la potencia que se generara en el area especificada. \n"
            "\n"
            "Datos: \n"
            f"Superficie disponible (Sr): {area} m^2 \n"
            f"Superficie reqierida segun la tecnologia del panel (Skwp): {technology} m^2/kWp\n"
            "\n"
            f"Calculo: \n"
            f"Ppg = Sr / Skwp = ({area}  / {technology} ) = "
            f"{self.approx_peak_power_value} \n"
        )

        ap = get_panel(id_panel).area

        if to_south:
            self.number_of_panels_value = int((area / (ap * 1.4)) + 1)
            self.number_of_panels = (
                "Al estar orientados al sur se requiere un aumento del 40% del "
                "area requerida. \n"
                "\n"
                "Datos: \n"
                f"Superficie disponible (Ad): {area} m^2 \n"
                f"Area del panel (Ap): {ap} m^2 \n"
                "\n"
                f"Calculo: \n"
                f"N = Ad / (Ap * 1.4) = ({area} / ({ap} * 1.4) ) = "
                f"{self.number_of_panels_value} \n"
            )

            self.peak_power_value = round(self.number_of_panels_value * get_panel(id_panel).peak_power, 2)
            self.peak_power = (
                "Potencia pico segun la cantidad de paneles que se usaran. \n"
                "\n"
                "Datos: \n"
                f"Numero de paneles (N): {self.number_of_panels_value} \n"
                f"Potencia nominal del panel (Pn): {get_panel(id_panel).peak_power} W \n"
                "\n"
                f"Calculo: \n"
                f"Pp = N * Pn = {self.number_of_panels_value} * {get_panel(id_panel).peak_power} = "
                f"{self.peak_power_value}"
            )
        else:

            self.number_of_panels_value = int((area / ap) + 1)
            self.number_of_panels = (
                "Datos: \n"
                f"Superficie disponible (Ad): {area} m^2 \n"
                f"Area del panel (Ap): {ap} m^2 \n"
                "\n"
                f"Calculo: \n"
                f"N = Ad / Ap = ({area} / {ap} ) = "
                f"{self.number_of_panels_value} \n"
            )

            self.peak_power_value = round(self.number_of_panels_value * get_panel(id_panel).peak_power * 0.8, 2)
            self.peak_power = ("Potencia pico segun la cantidad de paneles que se usaran. \n"
                               "\n"
                               "Al no estar los paneles orientados al sur, se hace una redupcion del 20%"
                               " de la energia generada. \n"
                               "\n"
                               "Datos: \n"
                               f"Numero de paneles (N): {self.number_of_panels_value} \n"
                               f"Potencia nominal del panel (Pn): {get_panel(id_panel).peak_power} wp \n"
                               "\n"
                               f"Calculo: \n"
                               f"Pp = N * Pn * 0.8 = {self.number_of_panels_value} * {get_panel(id_panel).peak_power} * 0.8 = "
                               f"{self.peak_power_value}")

        self.hsp = place
        self.userful_energy_value = round(self.hsp * self.peak_power_value, 2)
        self.userful_energy = (
            "Datos: \n"
            f"Hora solar pico segun el lugar (hsp): {place} h/día\n"
            f"Potencia pico (Pp): {self.peak_power_value} W \n"
            "\n"
            f"Calculo: \n"
            f"Eu = hsp * Pp = {self.hsp} * {self.peak_power_value} = "
            f"{self.userful_energy_value}"
        )

        self.controls = [
            ft.Text("Los paneles estan orientados al sur.") if to_south else ft.Text("Los paneles no estan orientados al sur.") ,
            ft.Text(f"Se definio un area de {area} m^2 disponibles para la creacion del sistema"),
            Result(f"Potencia pico segun la tecnologia: {self.approx_peak_power_value} kWp", self.approx_peak_power),
            Result(f"Numero de paneles: {self.number_of_panels_value}", self.number_of_panels),
            Result(f"Potencia pico segun la cantidad de paneles: {self.peak_power_value} W", self.peak_power),
            Result(f"Energia util: {self.userful_energy_value} Wh/día", self.userful_energy),
        ]


class CalcWithPeakPower(ft.Column):
    def __init__(self, peak_power: float, id_panel: str, place: float, to_south: bool):
        super().__init__()

        technology = (get_technology(get_panel(id_panel).cell_material)).get_min_surface_req()

        self.approx_area_value = round((peak_power/1000) * technology, 2)
        self.approx_area = (
            "Se realiza un calculo aproccimado segun la tecnologia del panel para obtener "
            "el area requerida para la potencia que se quiere obtener. \n"
            "\n"
            "Datos: \n"
            f"Potencia a instalar (Pinst): {peak_power/1000} kW\n"
            f"Superficie reqierida segun la tecnologia del panel (Skwp): {technology} m^2/kWp\n"
            "\n"
            f"Calculo: \n"
            f"Sr = Pinst * Skwp = ({peak_power/1000} * {technology}) = {self.approx_area_value} \n"
        )

        ap = get_panel(id_panel).area

        self.hsp = place
        self.userful_energy_value = round(self.hsp * peak_power, 2)
        self.userful_energy = (
            "Datos: \n"
            f"Hora solar pico segun el lugar (hsp): {place} m^2/kWp\n"
            f"Potencia pico (Pinst): {peak_power} W \n"
            "\n"
            f"Calculo: \n"
            f"Eu = hsp * Pinst = {self.hsp} * {peak_power} = {self.userful_energy_value}"
        )

        self.number_of_panels_value = int(
            self.userful_energy_value / (0.654 * self.hsp * get_panel(id_panel).peak_power) + 1)
        self.number_of_panels = (
            "\n"
            "Datos: \n"
            f"Energia util (Eu): {self.userful_energy_value} Wh/día\n"
            f"hora solar pico (hsp): {self.hsp} m^2/kWp\n"
            f"Potencia nominal del panel (Pn): {get_panel(id_panel).peak_power} W\n"
            "\n"
            f"Calculo: \n"
            f"N = Eu / (0.654 * hsp * Pn) = {self.userful_energy_value} / (0.654 * {self.hsp} * "
            f"{get_panel(id_panel).peak_power}) = {self.number_of_panels_value} \n"
        )

        if to_south:

            self.area_value = round(self.number_of_panels_value * get_panel(id_panel).area * 1.4, 2)
            self.area = (
                "Al estar orientados al sur se requiere un aumento del 40% del"
                " area requerida debido a la sombra que proyectan los paneles. \n"
                "\n"
                "Datos: \n"
                f"Numero de paneles (N): {self.number_of_panels_value} \n"
                f"Area del panel (Ap): {get_panel(id_panel).area} m^2\n"
                "\n"
                f"Calculo: \n"
                f"Ar = N * Ap = {self.number_of_panels_value} * {get_panel(id_panel).area} * 1.4 = "
                f"{self.area_value}"
            )
        else:
            self.peak_power = peak_power * 0.8

            self.area_value = round(float(self.number_of_panels_value * get_panel(id_panel).area), 2)
            self.area = (
                         "Datos: \n"
                         f"Numero de paneles (N): {self.number_of_panels_value} \n"
                         f"Area del panel (Ap): {get_panel(id_panel).area} m^2\n"
                         "\n"
                         f"Calculo: \n"
                         f"Ar = N * Ap = {self.number_of_panels_value} * {get_panel(id_panel).area} = "
                         f"{self.area_value}"
            )

        self.controls = [
            ft.Text("Los paneles estan orientados al sur.") if to_south else ft.Text("Los paneles no estan orientados al sur.") ,
            ft.Text(f"Se definio una potencia a instalar de {peak_power} W"),
            Result(f"Area requerida segun la tecnologia: {self.approx_area_value} m^2", self.approx_area),
            Result(f"Energia util: {self.userful_energy_value} Wh/día", self.userful_energy),
            Result(f"Numero de paneles: {self.number_of_panels_value}", self.number_of_panels),
            Result(f"Area requerida segun el numero de paneles: {self.area_value} m^2", self.area),
        ]

        if not to_south:
            self.controls.append(ft.Text("Se hace un descuento del 20% de la energia que generara el sistema debido a que los"
                    " paneles no estaran orientados al sur."))


class Economic(ft.Column):
    def __init__(self, id_panel, number_of_panels, userful_energy) -> None:
        super().__init__()

        panel: Panel = get_panel(id_panel)

        self.cost = round(panel.price * number_of_panels, 2)
        self.cost_details = (
            "\n"
            "Datos: \n"
            f"Costo del panel : {panel.price} cup \n"
            f"Cantidad de paneles que se usaran: {number_of_panels} \n"
            "\n"
            f"Calculo: \n"
            f"CSSFV = costo_del_panel * N = ({panel.price}  * {number_of_panels} ) = "
            f"{self.cost} cup\n"
        )

        userful_energy_year = round((userful_energy/1000) * 365, 2)

        self.income = round((panel.price_kwh_sen * userful_energy_year) , 2)
        self.income_details = (
            "\n"
            "Datos: \n"
            f"Energia util generada (Eu): {userful_energy} W/dia = "
            f"{userful_energy_year} kW/año \n"
            f"Precio del kWhSEN : {panel.price_kwh_sen} cup \n"
            "\n"
            f"Calculo: \n"
            f" Ig = Eu * Precio del kWhSEN = ({panel.price_kwh_sen} * "
            f"{userful_energy_year} ) = "
            f"{self.income} cup/año\n"
        )

        self.recovery = round(self.cost / self.income, 2)

        self.recovery_details = (
            "\n"
            "Datos: \n"
            f"CSSFV: {self.cost} cup \n"
            f"Ig : {self.income} cup/año \n"
            "\n"
            f"Calculo: \n"
            f" PSRI = CSSFV / Ig = ({self.cost} / {self.income} ) = "
            f"{self.recovery} años\n"
        )

        # Si el periodo de recuperacion en años da menor que 0, lo paso a meses
        # pero solo para mostrarlo
        if self.recovery < 1:
            self.recovery_text = f"{int(self.cost / (self.income/12))} meses aproximadamente"
        else:
            self.recovery_text = f"{self.recovery} años"

        self.controls = [
            ft.Text("Calculo economico: ", size=20, color=ft.colors.BLUE),
            Result(f"Costo del sistema: {self.cost} cup", self.cost_details),
            Result(f"Ingresos: {self.income} cup/año", self.income_details),
            Result(f"Periodo de recuperacion: {self.recovery_text}", self.recovery_details),
        ]


class FinalFace(ft.Column):
    def __init__(self):
        super().__init__()

        self.progress = 0
        self.button_progress = ft.ElevatedButton("Planificacion", color=ft.colors.BLACK,
                                                 bgcolor=ft.colors.GREY, on_click=self.change_progress)

        self.name = ft.TextField(label="Identificador del sistema")
        self.description = ft.TextField(label="Descripcion", min_lines=5, max_lines=10)

        self.controls= [
            ft.Row([self.name,
                ft.Row([self.button_progress, ft.Text("Estado del sistema", color=ft.colors.GREY)])],
                    wrap=True),
            ft.Column([self.description, ft.Text("No es obligatorio", color=ft.colors.GREY)],)
        ]

    def change_progress(self, e):
        if self.progress == 0:
            self.progress = 1
            self.button_progress.bgcolor = ft.colors.YELLOW
            self.button_progress.text = "Construccion"

        elif self.progress == 1:
            self.progress = 2
            self.button_progress.bgcolor = ft.colors.GREEN
            self.button_progress.text = "Terminado"

        elif self.progress == 2:
            self.progress = 0
            self.button_progress.bgcolor = ft.colors.GREY
            self.button_progress.text = "Planificacion"

        self.update()