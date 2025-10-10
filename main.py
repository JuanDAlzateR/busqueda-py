import flet as ft
from app.navigation import get_page

def main(page: ft.Page):
    page.title = "Búsqueda del tesoro 💕"
    page.window_width = 420
    page.window_height = 720
    page.scroll = "auto"
    page.theme_mode = "light"
    page.bgcolor = "#FFF5F8"

    # Estado del juego
    page.session.set("current_screen", "home")

    # Navegación
    def navigate_to(screen_name):
        page.session.set("current_screen", screen_name)
        page.views.clear()
        page.views.append(get_page(page, screen_name, navigate_to))
        page.update()

    # Pantalla inicial
    navigate_to("home")

ft.app(target=main)
