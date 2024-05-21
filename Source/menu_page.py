import datetime

import flet as ft

from .components import Title
from .view import View

class MenuButton(ft.OutlinedButton):
    def __init__(self, text, **kwargs):
        super().__init__(text, **kwargs)
        self.style = ft.ButtonStyle(
            color=ft.colors.BLACK,
            shape=ft.RoundedRectangleBorder(radius=0)
        )

class MenuPage(View):
    title = "SysGremio"
    def generate_main_content(self):
        return ft.Column(
            horizontal_alignment=ft.alignment.center,
            controls=[
                Title(self.title),
                ft.Container(
                    alignment=ft.alignment.center,
                    expand=True,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            MenuButton('Iniciar Votação'),
                            MenuButton('Configurar chapas'),
                            MenuButton('Sair'),
                        ]
                    )
                ),
                ft.Container(
                    alignment=ft.alignment.center,
                    height=100,
                    content=ft.Text(
                        '@felifelps.dev\nEx-aluno do curso de informática',
                        text_align=ft.TextAlign.CENTER,
                    )
                )
            ],
        )
