import flet as ft

class View(ft.View):
    page = None
    title = 'Title'
    content_controls = []
    allow_url = True
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.drawer = self.page.drawer
        self.controls = [
            ft.Container(
                bgcolor=ft.colors.BACKGROUND,
                expand=True,
                content=self.generate_main_content()
            )
        ]

    def on_pre_view(self):
        pass

    def generate_main_content(self):
        return ft.Column(
            spacing=0,
            controls=[
                Title(self.title),
                ft.Container(
                    alignment=ft.alignment.center,
                    expand=True,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=self.content_controls
                    )
                ),
                ft.Container(
                    alignment=ft.alignment.bottom_center,
                    height=100,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.TextButton(
                                content=ft.Text(
                                    '@felifelps.dev\nEx-aluno do curso de informática',
                                    text_align=ft.TextAlign.CENTER,
                                ),
                                url="https://www.instagram.com/felifelps.dev/" if self.allow_url else "",
                                style=ft.ButtonStyle(overlay_color=ft.colors.BACKGROUND),
                            ),
                            
                        ]
                    )
                )
            ],
        )

class Title(ft.Container):
    def __init__(self, title, **kwargs):
        super().__init__(**kwargs)
        self.content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Image(
                            src='icon.png',
                            width=100,
                            height=100
                        ),
                        ft.Text(
                            'SysGremio',
                            size=40,
                        )
                    ]
                ),
                ft.Divider(),
                ft.Text(
                    title,
                    size=30,
                    visible=bool(title)
                )
            ]
        )
        self.alignment = ft.alignment.top_center
