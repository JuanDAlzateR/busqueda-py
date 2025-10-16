import flet as ft

def main(page: ft.Page):
    page.title = "Close Dialog Example"

    def close_dlg(e):
        dlg.open = False  # Set the dialog's open property to False
        page.update()     # Update the page to reflect the change

    dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text("My Dialog"),
        content=ft.Text("This is a sample dialog."),
        actions=[
            ft.TextButton("Close", on_click=close_dlg),
        ],
    )

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    page.add(
        ft.ElevatedButton("Open Dialog", on_click=open_dlg)
    )

ft.app(target=main)