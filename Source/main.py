import flet as ft

from .components import Message
from .menu_page import MenuPage
from .configure_page import ConfigurePage
from .view import View
from .voting_page import VotingPage

def main(page: ft.Page):
    page.title = "SysGremio"
    page.window_full_screen = True
    page.theme = ft.Theme(color_scheme_seed='gray')
    page.theme_mode = 'light'
    page.padding = 0
    page.spacing = 0
    page.snack_bar = Message(page)

    View.page = page

    page.views.extend([
        MenuPage(route='/menu'),
        ConfigurePage(route='/conf'),
        VotingPage(route='/vote')
    ])

    def on_route_change(_):
        page.views.sort(key=lambda view: view.route == page.route)
        page.views[-1].page = page
        page.views[-1].on_pre_view()
        page.update()

    page.on_route_change = on_route_change
    page.go('/vote')
