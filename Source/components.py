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

class NavigationDrawer(ft.NavigationDrawer):
    routes = ['/clients', '/register']
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controls=[
            ft.Stack(
                height=85,
                controls=[
                    ft.Image(
                        src='img/smaller_logo.png',
                        width=150,
                        height=75,
                        bottom=0,
                    )
                ]
            ),
            ft.Divider(
                color=ft.colors.WHITE,
                thickness=2
            ),
            ft.NavigationDrawerDestination(label="CLIENTES CADASTRADOS"),
            ft.NavigationDrawerDestination(label="CADASTRAR CLIENTE"),
            ft.TextButton(
                'SAIR',
                on_click=self.logout
            ),
            ft.Divider(),
            ft.TextButton(
                '@dev.syst',
                url='https://www.instagram.com/dev.syst/'
            )
        ]

        self.on_change = self.change

    def change(self, e):
        e.page.close_drawer()
        e.page.go(self.routes[self.selected_index])

    def logout(self, e):
        e.page.close_drawer()
        e.page.client_storage.clear()
        e.page.go('/login')

class CustomButton(ft.Container):
    def __init__(self, text, on_click, **kwargs):
        super().__init__(**kwargs)
        self.content = ft.TextButton(
            content=ft.Text(
                text,
                font_family='Garet',
                color=ft.colors.WHITE
            ),
            on_click=on_click
        )
        self.width = 200
        self.height = 45
        self.border = kwargs.get(
            'border',
            ft.border.all(2, ft.colors.WHITE)
        )
        self.border_radius = 50
        self.bgcolor = kwargs.get(
            'bgcolor',
            ft.colors.GREY_800
        )

class CustomTextField(ft.TextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        bgcolor = '#dddddd'
        self.label_style = ft.TextStyle(
            color = ft.colors.GREY_800
        )
        self.color = ft.colors.GREY_800
        self.text_style = ft.TextStyle(
            font_family = "Garet"
        )
        self.focused_border_color = bgcolor
        self.border = ft.InputBorder.OUTLINE
        self.border_color = bgcolor
        self.border_radius = 90
        self.filled = True
        self.bgcolor = bgcolor
        self.height = 45
        self.expand = True
        self.expand_loose = True

class ClientTextField(CustomTextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_size = 15
        self.disabled = True

class DateField(ft.Container):
    def __init__(self, page, value='', disabled=False, **kwargs):
        super().__init__(**kwargs)

        self._value = value

        def on_change(e):
            self.value = self.date_picker.value
            e.page.update()

        self.date_picker = ft.DatePicker(
            on_change=on_change,
            value=value,
            last_date=datetime.datetime.today()
        )
        page.overlay.append(self.date_picker)

        self.text = ClientTextField(
            label='Data de nascimento',
            value=value if isinstance(value, str) else f'{value:%d/%m/%Y}',
            color=ft.colors.GREY_800,
            text_style=ft.TextStyle(
                font_family = "Garet"
            ),
            disabled=True,
        )

        self.alignment = ft.alignment.center
        self.content = self.text
        self.height = 45
        if not disabled:
            self.on_click = lambda e: self.date_picker.pick_date()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self.text.value = value if isinstance(value, str) else f'{value:%d/%m/%Y}'
