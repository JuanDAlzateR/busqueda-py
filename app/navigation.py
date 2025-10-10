from screens.home_screen import HomeScreen
from screens.level_screen import LevelScreen
from screens.success_screen import SuccessScreen

def get_page(page, screen_name, navigate_to):
    if screen_name == "home":
        return HomeScreen(page, navigate_to)
    elif screen_name.startswith("level"):
        level_id = screen_name.split("_")[1]
        return LevelScreen(page, navigate_to, level_id)
    elif screen_name == "success":
        return SuccessScreen(page, navigate_to)