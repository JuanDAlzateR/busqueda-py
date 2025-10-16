import flet as ft
from app.navigation import get_page
from app.utils.utils import update_time

def main(page: ft.Page):
    page.title = "Búsqueda del tesoro 💕"
    page.session.set("stats", {"amor": 10, "dinero": 5, "fe": 7, "tiempo": 3})
    page.window_width = 420
    page.window_height = 720
    page.scroll = "auto"
    page.theme_mode = "light"
    page.bgcolor = "#FFF5F8"

    # Estado del juego
    page.session.set("current_screen", "home")
    update_time(page)


    # Navegación
    def navigate_to(screen_name):
        page.session.set("current_screen", screen_name)
        page.views.clear()
        page.views.append(get_page(page, screen_name, navigate_to))
        page.update()

    # Pantalla inicial
    navigate_to("home")

ft.app(target=main)
