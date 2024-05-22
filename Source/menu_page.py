import flet as ft

from .components import CustomButton
from .view import View

class MenuPage(View):
    title = "SysGremio"
    content_controls = [
        CustomButton('Iniciar Votação'),
        CustomButton(
            'Configurar chapas',
            on_click=lambda e: e.page.go('/conf')
        ),
        CustomButton(
            'Sair',
            on_click=lambda e: e.page.window_close()
        ),
    ]
