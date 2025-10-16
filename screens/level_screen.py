# screens/level_screen.py  (parche recomendado)
import flet as ft
import asyncio
import threading
from app.data import LEVELS
from app.utils.utils import check_password
from app.utils.utils import add_stats
from app.utils.qr import open_qr_scanner
from app.styles import title_style, text_style
from components.stats_bar import StatsBar

def LevelScreen(page, navigate_to, level_id):
    stats = page.session.get("stats")
    level = LEVELS.get(level_id) if level_id in LEVELS else LEVELS.get(str(level_id))
    input_field = ft.TextField(label="Escribe la palabra clave ✨", width=250)

    def show_snack(msg):
        snack = ft.SnackBar(ft.Text(msg))
        page.open(snack)   # <<-- usado en lugar de page.snack_bar = ...
    
    def scan_qr(e):
        # Evita que el UI se congele usando un hilo
        def run_scan():
            result = open_qr_scanner()
            if result:
                page.snack_bar = ft.SnackBar(ft.Text(f"Código leído: {result} ✅"), open=True)
                page.update()
            else:
                page.snack_bar = ft.SnackBar(ft.Text("No se detectó ningún código 😅"), open=True)
                page.update()

        threading.Thread(target=run_scan).start()
    
    def on_submit(e):
        try:
            password = (input_field.value or "").strip()
            print(f"[DEBUG] on_submit invoked. level_id={level_id!r}, password={password!r}")
        except Exception as ex:
            print("[ERROR] reading input_field.value:", ex)
            show_snack("Error leyendo el campo. Revisa la consola.")
            return

        if not password:
            show_snack("Por favor escribe una palabra clave ✍️")
            return

        try:
            ok = check_password(level_id, password, LEVELS)
        except Exception as ex:
            print("[ERROR] check_password raised:", ex)
            show_snack("Error interno validando contraseña (ver consola).")
            return

        if ok:
            next_levels = level.get("next", [])
            print(f"[DEBUG] password OK. next_levels = {next_levels!r}")
            if len(next_levels) == 1:
                ns = next_levels[0]
                # usa el mismo formato que main.navigate_to (sin slash)
                route = "success" if ns == "success" else f"level_{ns}"
                print(f"[DEBUG] navigating to {route}")
                navigate_to(route)
                page.update()
                return

            # varias rutas: construir dialog y abrirlo con page.open_dialog
            buttons = []
            for n in next_levels:
                target = "success" if n == "success" else f"level_{n}"
                def make_onclick(t=target):
                    async def _onclick(ev):
                        page.close(dlg)   
                        # usar un pequeño delay para que Flet procese el cierre
                        await asyncio.sleep(0.1)
                        navigate_to(t)
                        update_stats(page,"tiempo",2)
                        page.update()                        
                    return _onclick
                buttons.append(ft.ElevatedButton(f"Ir a {n}", on_click=make_onclick()))

            dlg = ft.AlertDialog(title=ft.Text("Elige tu siguiente destino ❤️"), content=ft.Column(buttons))
            page.open(dlg)   # <<-- usado en lugar de asignar page.dialog
        else:
            print("[DEBUG] contraseña incorrecta")
            show_snack("Contraseña incorrecta 😅")

    # layout
    return ft.View(       
        f"/level_{level_id}",  # ruta de la View (esto está bien)
        controls=[
            StatsBar(stats),
            ft.Column(
                [
                    ft.Image(src=level.get("image",""), width=200) if level.get("image") else ft.Container(),
                    ft.Text(level.get("text",""), style=text_style(), text_align="center"),
                    input_field,
                    ft.ElevatedButton("Confirmar 💫", on_click=on_submit, bgcolor="#E91E63", color="white"),
                    ft.ElevatedButton("📷 Escanear código", on_click=scan_qr, bgcolor="#2196F3", color="white"),
                ],
                alignment="center",
                horizontal_alignment="center",
                expand=True,
            )
        ],
    )