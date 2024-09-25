import flet as ft


from src.modules.panel_module import Panel
from src.modules.hsp_module import HSP
from src.modules.technology_module import Technology


# todo arreglar esto para los textos que no quepan en pantalla
def info_container(info: str, value):
    return ft.Row([
        ft.Container(content=ft.Text(f"{info} :", size=15),
                     bgcolor=ft.colors.BLUE_100, padding=5, border_radius=5),
        ft.Text(value, size=15)
    ], scroll=ft.ScrollMode.ADAPTIVE)


class EntityInfo(ft.Container):
    def __init__(self, entity: Panel | HSP | Technology):
        """
        Mustra la informacion de los atributos de la entidad.

        :param entity: entidad a mostrar
        """

        super().__init__()

        # Panel
        if isinstance(entity, Panel):
            self.entity: Panel = entity

            # Atributos
            technology = info_container("potencia pico", self.entity.peak_power)
            area = info_container("material de las celdas", self.entity.cell_material)
            area = info_container("area", self.entity.area)
            price = info_container("precio", self.entity.price)
            price_kwh_sen = info_container("precio del kwh SEN", self.entity.price_kwh_sen)

            self.info = [technology, area, area, price, price_kwh_sen]

        # Hora solar pico
        if isinstance(entity, HSP):
            self.entity: HSP = entity

            # Atributos
            place = info_container("lugar", self.entity.place)
            value = info_container("valor", self.entity.value)

            self.info = [place, value]

        # Tecnologia
        if isinstance(entity, Technology):
            self.entity: Technology = entity

            # Atributos
            technology = info_container("tecnologia", self.entity.technology)
            area = info_container("area requerida",
                                           f"{self.entity.surface[0]} - {self.entity.surface[1]}")

            self.info = [technology, area]

        # bordes y padding
        self.border = ft.border.all(1, ft.colors.GREY)
        self.border_radius = 5
        self.padding = 10

        self.content = ft.Column(self.info)


class WhereUsed(ft.Container):
    def __init__(self, entity: Panel | HSP | Technology):
        """
        Muestra los sistemas donde se usa esta entidad.

        :param entity:
        """

        super().__init__()

        systems = []

        # todo cambiar esto para saber donde se usa cada entidad

        # if isinstance(entity, Panel):
        #     self.entity: Panel = entity
        #
        #     systems = find_panel(self.entity.id_panel)
        #
        # if isinstance(entity, Hsp):
        #     self.entity: Hsp = entity
        #
        #     systems = db.find_hsp(self.entity.place)
        #
        # if isinstance(entity, Technology):
        #     self.entity: Technology = entity
        #
        #     systems = db.find_technology(self.entity.technology)

        # bordes y padding
        self.border = ft.border.all(1, ft.colors.GREY)
        self.border_radius = 5
        self.padding = 10

        # todo cambiar cuando ya se pueda añadir sistemas
        if systems:
            pass
        else:
            self.content = ft.Text("No se usa en ningun sistema.")