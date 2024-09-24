import flet as ft


class MyDataRow(ft.CupertinoButton):
    def __init__(self, row: ft.Row):
        super().__init__()
        self.content = row


class MyDataTable(ft.Container):
    def __init__(self, spacing=10):
        super().__init__()
        self.head = []

        self._row_head = ft.Row(controls=self.head, spacing=spacing)

        self._rows = []

        self.content = ft.Column([self._row_head, ft.Column(self._rows)])

    def add_row(self, cells: list[ft.Control]):
        if len(cells) == len(self.head):
            self._rows.append(MyDataRow(
                ft.Row(cells, spacing=self._row_head.spacing)
            ))
        else:
            print("Error: la cantidad de celdas de cada fila nueva debe coincidir con las del encabezado...")
