from .components import CustomButton
from .models import Chapa
from .view import View

class MenuPage(View):
    title = ""
    start_voting_button = CustomButton(
        'Iniciar Votação',
        on_click=lambda e: e.page.go('/vote')
    )
    configure_button = CustomButton(
        'Configurar chapas',
        on_click=lambda e: e.page.go('/conf')
    )
    content_controls = [
        start_voting_button,
        configure_button,
        CustomButton(
            'Sair',
            on_click=lambda e: e.page.window_close()
        ),
    ]

    def on_pre_view(self, e):
        non_finished_voting = False
        for chapa in Chapa.select():
            if chapa.votes:
                non_finished_voting = True

        self.start_voting_button.text = ('Continuar' if non_finished_voting else 'Iniciar') + ' Votação'
        self.configure_button.visible = not non_finished_voting
