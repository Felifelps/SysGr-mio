import flet as ft

from .components import CustomButton
from .control import Control
from .models import Chapa
from .view import View

class VotingPage(View):
    title = "Votação"
    allow_url = False
    def __init__(self, **kwargs):
        self.audio = ft.Audio(src="assets/audio.mp3", volume=1)
        self.page.overlay.append(self.audio)

        self.radios = ft.Column(
            controls=[]
        )
        self.radio_group = ft.RadioGroup(
            content=self.radios
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
        self.password_field = ft.TextField(
            label='Senha',
            password=True,
            autofocus=True
        )
        self.password_dialog = ft.AlertDialog(
            title=ft.Text('Finalizar a votação? (Irreversível)'),
            modal=True,
            content=self.password_field,
            actions=[
                ft.TextButton(
                    'Cancelar', 
                    on_click=lambda e: e.page.close_dialog()
                ),
                ft.TextButton('Finalizar', on_click=self.check_password),
            ]
        )

        self.votes_count = ft.Text()
        self.content_controls = [
            self.votes_count,
            CustomButton(
                'Votar',
                on_click=self.open_first_dialog
            ),
            CustomButton(
                'Finalizar Votação',
                on_click=self.open_password_dialog
            )
        ]
        super().__init__(**kwargs)

    def on_pre_view(self):
        self.page.window_prevent_close = True
        votes = 0
        self.radios.controls.clear()

        for chapa in Chapa.select():
            self.radios.controls.append(
                ft.Radio(value=chapa.id, label=chapa.name)
            )
            votes += chapa.votes
        self.votes_count.value = f'Votos computados: {votes}'

        self.radios.height = len(self.radios.controls) * 50

        Control.start_voting()

        self.page.snack_bar.message('Votação iniciada')

        return super().on_pre_view()

    def open_password_dialog(self, e):
        self.password_field.value = ""
        e.page.dialog = self.password_dialog
        self.password_dialog.open = True
        e.page.update()

    def check_password(self, e):
        check = Control.check_credentials(self.password_field.value)
        e.page.close_dialog()
        if check:
            e.page.window_prevent_close = False
            return e.page.go('/result')
        e.page.snack_bar.message('Senha inválida', 'error')

    def open_first_dialog(self, e):
        e.page.dialog = self.first_dialog
        self.first_dialog.open = True
        e.page.update()

    def open_second_dialog(self, e):
        if not self.radio_group.value:
            return e.page.snack_bar.message('Escolha uma opção')
        e.page.dialog = self.second_dialog
        self.second_dialog.open = True
        e.page.update()

    def vote(self, e):
        chapa = Chapa.get_by_id(self.radio_group.value)
        chapa.votes += 1
        chapa.save()

        self.radio_group.value = None

        self.page = e.page
        self.on_pre_view()

        self.audio.play()

        e.page.close_dialog()
        e.page.update()
