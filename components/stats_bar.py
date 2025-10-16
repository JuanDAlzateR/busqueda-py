import flet as ft

def StatsBar(stats):
    def make_stat(icon, value, max_value):
        return ft.Row(
            [
                ft.Text(icon, size=20),
                ft.Text(f"{value}/{max_value}", size=16, weight="bold"),
            ],
            spacing=5,
            alignment="center",
        )

    return ft.Row(
        [
            make_stat("❤️", stats["amor"], 20),
            make_stat("💰", stats["dinero"], 10),
            make_stat("🙏", stats["fe"], 10),
            make_stat("⏳", stats["tiempo"], 10),
        ],
        alignment="spaceEvenly",
        vertical_alignment="center",
    )