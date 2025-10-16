import flet as ft
from app.data import LEVELS
from app.utils import check_password
from app.styles import title_style, text_style

def LevelScreen(page, navigate_to, level_id):
    level = LEVELS[level_id]
    input_field = ft.TextField(label="Escribe la palabra clave ✨", width=250)

    def on_submit(e):
        password = (input_field.value or "").strip()
        print(f"[DEBUG] on_submit invoked. level_id={level_id!r}, password={password!r}")

        if not password:
            show_snack("Por favor escribe una palabra clave ✍️")
            return

        ok = check_password(level_id, password, LEVELS)

        if ok:
            next_levels = level.get("next", [])
            print(f"[DEBUG] password OK. next_levels = {next_levels!r}")

            if len(next_levels) == 1:
                ns = next_levels[0]
                route = "/success" if ns == "success" else f"/level_{ns}"
                print(f"[DEBUG] navigating to {route}")
                navigate_to(route)
                page.update()
                return

            # varias rutas posibles
            buttons = []
            for n in next_levels:
                target = "/success" if n == "success" else f"/level_{n}"

                def make_onclick(t=target):
                    def _onclick(ev):
                        page.close_dialog()
                        navigate_to(t)
                        page.update()
                    return _onclick

                buttons.append(ft.ElevatedButton(f"Ir a {n}", on_click=make_onclick()))

            dlg = ft.AlertDialog(
                title=ft.Text("Elige tu siguiente destino ❤️"),
                content=ft.Column(buttons)
            )
            page.open_dialog(dlg)
        else:
            print("[DEBUG] contraseña incorrecta")
            show_snack("Contraseña incorrecta 😅")

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

