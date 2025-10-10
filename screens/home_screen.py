import flet as ft
from app.styles import title_style, text_style

def HomeScreen(page, navigate_to):
    return ft.View(
        "/home",
        controls=[
            ft.Column(
                [
                    ft.Image(src="assets/images/portada.png", width=250),
                    ft.Text("Búsqueda del tesoro 💕", style=title_style(), text_align="center"),
                    ft.Text(
                        "Una aventura romántica para descubrir el mayor tesoro: su amor.",
                        style=text_style(),
                        text_align="center",
                    ),
                    ft.ElevatedButton(
                        "Comenzar aventura 💌",
                        on_click=lambda _: navigate_to("level_1"),
                        bgcolor="#E91E63",
                        color="white",
                        width=200,
                    ),
                ],
                alignment="center",
                horizontal_alignment="center",
                expand=True,
            )
        ],
    )