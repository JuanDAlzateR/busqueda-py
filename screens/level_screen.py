import flet as ft
from app.data import LEVELS
from app.utils import check_password
from app.styles import title_style, text_style

def LevelScreen(page, navigate_to, level_id):
    level = LEVELS[level_id]
    input_field = ft.TextField(label="Escribe la palabra clave ✨", width=250)

    def on_submit(e):
        if check_password(level_id, input_field.value, LEVELS):
            next_levels = level["next"]
            if len(next_levels) == 1:
                navigate_to(f"level_{next_levels[0]}" if next_levels[0] != "success" else "success")
            else:
                # Si hay varias rutas posibles, muestra opciones
                page.dialog = ft.AlertDialog(
                    title=ft.Text("Elige tu siguiente destino ❤️"),
                    content=ft.Column(
                        [
                            ft.ElevatedButton(
                                f"Ir a ruta {n}",
                                on_click=lambda _, n=n: (
                                    setattr(page.dialog, "open", False),
                                    navigate_to(f"level_{n}")
                                ),
                            )
                            for n in next_levels
                        ]
                    ),
                )
                page.dialog.open = True
                page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Contraseña incorrecta 😅"), open=True)
            page.update()

    return ft.View(
        f"/level_{level_id}",
        controls=[
            ft.Column(
                [
                    ft.Image(src=level["image"], width=200),
                    ft.Text(level["text"], style=text_style(), text_align="center"),
                    input_field,
                    ft.ElevatedButton("Confirmar 💫", on_click=on_submit, bgcolor="#E91E63", color="white"),
                ],
                alignment="center",
                horizontal_alignment="center",
                expand=True,
            )
        ],
    )