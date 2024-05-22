import os

import flet as ft

from .components import CustomButton
from .control import Control
from .view import View

class ResultPage(View):
    title = "Resultado"
    def __init__(self, **kwargs):
        self.file_path = ''
        self.results = ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        self.votes_count = ft.Text()
        self.content_controls = [
            ft.Container(
                border=ft.border.all(
                    1, ft.colors.GREY_600
                ),
                padding=ft.padding.all(30),
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        self.votes_count,
                        self.results
                    ]
                )
            ),
            CustomButton(
                'Abrir arquivo com Resultado',
                on_click=lambda _: os.system(f'notepad "{self.file_path}"')
            ),
            CustomButton(
                'Sair',
                on_click=lambda e: e.page.go('/menu')
            )
        ]

        super().__init__(**kwargs)


    def on_pre_view(self):
        results, votes, self.file_path = Control.get_and_save_results()

        self.results.controls = [ft.Text(r) for r in results]
        self.votes_count.value = f'Votos computados: {votes}'

        self.page.snack_bar.message(
            'Votação Finalizada com sucesso!\nResultado salvo na sua área de trabalho', 
            'success'
        )

        return super().on_pre_view()
