import flet as ft

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
