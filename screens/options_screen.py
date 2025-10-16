import flet as ft
from app.styles import title_style, text_style

def OptionsScreen(page, navigate_to, previous_level):
    return ft.View(
        "/home",
        controls=[
            ft.Column(
                [
                    ft.Image(src="assets/images/portada.png", width=250),
                    ft.Text("💕 Decisiones:", style=title_style(), text_align="center"),
                    ft.Text(
                        "Escoje una de las siguientes opciones:",
                        style=text_style(),
                        text_align="center",
                    ),
                    
                    next
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