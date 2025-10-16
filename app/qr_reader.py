import flet as ft
from pyzbar.pyzbar import decode
from PIL import Image
import io

def main(page: ft.Page):
    result_text = ft.Text("Escanea un código QR 📸")

    def on_file_pick(e: ft.FilePickerResultEvent):
        if e.files:
            file = e.files[0]
            content = file.content
            image = Image.open(io.BytesIO(content))
            decoded = decode(image)
            if decoded:
                data = decoded[0].data.decode("utf-8")
                result_text.value = f"✅ Código detectado: {data}"
            else:
                result_text.value = "❌ No se detectó ningún código QR."
            page.update()

    picker = ft.FilePicker(on_result=on_file_pick)
    page.overlay.append(picker)

    def open_camera(e):
        picker.pick_files(
            allow_multiple=False,
            file_type=ft.FilePickerFileType.IMAGE,
            camera=True  # fuerza cámara en Android/iOS
        )

    page.add(
        ft.Column(
            [
                result_text,
                ft.ElevatedButton("Escanear QR", on_click=open_camera),
            ],
            alignment="center",
            horizontal_alignment="center",
        )
    )

ft.app(target=main)