import datetime

import flet as ft

class Title(ft.Container):
    def __init__(self, title, **kwargs):
        super().__init__(**kwargs)
        self.content = ft.Text(
            title, 
            size=40,
        )
        self.alignment = ft.alignment.center
        self.height = 200

class Message(ft.SnackBar):
    colors = {
        'default': ft.colors.GREY_800,
        'success': ft.colors.GREEN,
        'error': ft.colors.RED
    }
    def __init__(self, page, **kwargs):
        super().__init__(
            content=ft.Text(
                'Default message',
                color=ft.colors.GREY_100
            ),
            shape=ft.RoundedRectangleBorder(radius=50),
            margin=10,
            bgcolor=ft.colors.GREY_800,
            **kwargs
        )
        self.page = page

    def message(self, text, color='default'):
        self.content.value = text
        self.bgcolor = self.colors[color]
        self.open = True
        self.page.update()


class CustomButton(ft.OutlinedButton):
    def __init__(self, text, **kwargs):
        super().__init__(text, **kwargs)
        self.style = ft.ButtonStyle(
            color=ft.colors.BLACK,
            shape=ft.RoundedRectangleBorder(radius=0)
        )
