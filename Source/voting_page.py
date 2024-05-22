import flet as ft

from .components import CustomButton
from .models import Chapa
from .view import View

class VotingPage(View):
    title = "Votação"
    def __init__(self, **kwargs):
        radios = [ft.Radio(value=c.id, label=c.name) for c in Chapa.select()]
        self.radio_group = ft.RadioGroup(
            content=ft.Column(
                controls=radios
            )
        )
        self.first_dialog = ft.AlertDialog(
            title=ft.Text('Selecione:'),
            content=self.radio_group,
            modal=True,
            actions=[
                ft.TextButton('Votar', on_click=self.open_second_dialog)
            ]
        )
        self.second_dialog = ft.AlertDialog(
            title=ft.Text('Confirmar seu voto?'),
            modal=True,
            actions=[
                ft.TextButton('Cancelar', on_click=self.open_first_dialog),
                ft.TextButton('Confirmar', on_click=self.vote),
            ]
        )
        self.content_controls = [
            CustomButton(
                'Votar',
                on_click=self.open_first_dialog
            ),
            CustomButton(
                'Finalizar Votação'
            )
        ]
        super().__init__(**kwargs)

    def open_first_dialog(self, e):
        e.page.dialog = self.first_dialog
        self.first_dialog.open = True
        e.page.update()

    def open_second_dialog(self, e):
        e.page.dialog = self.second_dialog
        self.second_dialog.open = True
        e.page.update()

    def vote(self, e):
        e.page.close_dialog()
