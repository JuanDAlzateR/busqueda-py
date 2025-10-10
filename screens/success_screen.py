import flet as ft
from app.styles import title_style

def SuccessScreen(page, navigate_to):
    return ft.View(
        "/success",
        controls=[
            ft.Column(
                [
                    ft.Image(src="assets/images/corazon.png", width=250),
                    ft.Text("💍 ¡Felicidades!", style=title_style(), text_align="center"),
                    ft.Text(
                        "Has completado la Carrera del Amor.\nAhora es momento de hacer la gran pregunta 💖",
                        text_align="center",
                    ),
                    ft.ElevatedButton(
                        "Volver al inicio",
                        on_click=lambda _: navigate_to("home"),
                        bgcolor="#E91E63",
                        color="white",
                    ),
                ],
                alignment="center",
                horizontal_alignment="center",
                expand=True,
            )
        ],
    )