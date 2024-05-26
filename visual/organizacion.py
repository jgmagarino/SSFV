import flet as ft
from funciones import mi_gestor_pickle as pkl

l = pkl.cargar_informacion_pickle("../salva/Sistemas")

column_sistemas = ft.Column(
    [ft.Text("Sistemas")]
)

column_paneles = ft.Column(
    [ft.Text("Paneles")]
)

column_tecgnologias = ft.Column(
    [ft.Text("Tecgnologias")]
)

column_hsp = ft.Column(
    [ft.Text("Sistemas")]
)

column_configuracion = ft.Column(
    [ft.Text("Configuracion")]
)

column_ayuda = ft.Column(
    [ft.Text("Ayuda")]
)

arry_columns: list[ft.Column] = [column_sistemas, column_paneles, column_tecgnologias,
                                 column_hsp, column_configuracion, column_ayuda]
