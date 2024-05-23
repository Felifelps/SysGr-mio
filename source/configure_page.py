import flet as ft

from .components import CustomButton
from .models import Chapa
from .view import View

class ConfigurePage(View):
    title = "Configurar Chapas"
    chapa_field = ft.TextField(
        label='Nome da chapa'
    )
    list_view = ft.ListView()
    def __init__(self, **kwargs):
        self.content_controls = [
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    self.chapa_field,
                    CustomButton(
                        'Criar Chapa',
                        on_click=self.check_for_new_chapa
                    )
                ]
            ),
            ft.Container(
                width=450,
                border=ft.border.all(
                    1, ft.colors.GREY_600
                ),
                content=self.list_view
            ),
            CustomButton(
                'Voltar',
                on_click=lambda e: e.page.go('/menu')
            )
        ]
        super().__init__(**kwargs)

    def check_for_new_chapa(self, e):
        value = self.chapa_field.value.strip()
        if value and not Chapa.get_or_none(name=value):
            self.chapa_field.value = ''
            Chapa.create(name=value)
            self.on_pre_view()
            e.page.update()

    def on_pre_view(self):
        controls = [ChapaCard(c.get_data(), self.delete) for c in Chapa.select()]
        self.list_view.controls = controls
        return super().on_pre_view()

    def delete(self, e, chapa_id):
        if len(self.list_view.controls) == 2:
            return e.page.snack_bar.message('Devem haver duas chapas, no mínimo')

        Chapa.delete_by_id(chapa_id)
        self.on_pre_view()
        e.page.update()


class ChapaCard(ft.ListTile):
    def __init__(self, data, delete_func, **kwargs):
        super().__init__(**kwargs)
        self.data = data
        self.title = ft.Text(
            data['name']
        )
        self.trailing = ft.IconButton(
            ft.icons.DELETE,
            on_click=lambda e: delete_func(e, data['id'])
        )
