import flet as ft
from .components import Title

class View(ft.View):
    page = None
    title = 'Title'
    content_controls = []
    allow_url = True
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.drawer = self.page.drawer
        self.controls = [ft.Container(
            bgcolor=ft.colors.WHITE70,
            expand=True,
            content=ft.Stack(
                controls=[
                    self.generate_main_content()
                ]
            )
        )]

    def on_pre_view(self):
        pass

    def generate_main_content(self):
        return ft.Column(
            horizontal_alignment=ft.alignment.center,
            controls=[
                Title(self.title),
                ft.Container(
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(top=140),
                    expand=True,
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=self.content_controls
                    )
                ),
                ft.Container(
                    alignment=ft.alignment.center,
                    height=100,
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.TextButton(
                                '@felifelps.dev',
                                url="https://www.instagram.com/felifelps.dev/" if self.allow_url else "",
                                style=ft.ButtonStyle(overlay_color=ft.colors.BACKGROUND)
                            ),
                            ft.Text(
                                'Ex-aluno do curso de informática',
                                text_align=ft.TextAlign.CENTER,
                            )
                        ]
                    )
                )
            ],
        )
