import flet as ft

class View(ft.View):
    page = None
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
        return ft.Text('Generate main content')
