from datetime import datetime

def check_password(level_id, user_input, levels):
    """Verifica si la contraseña es correcta para una pista dada."""
    correct = levels[level_id]["password"].strip().lower()
    return user_input.strip().lower() == correct

def add_stats(page,stat_type,n):
    stats = page.session.get("stats")
    stats[stat_type] += n
    page.session.set("stats", stats)
    page.update()

def set_stats(page,stat_type,n):
    stats = page.session.get("stats")
    stats[stat_type] = n
    page.session.set("stats", stats)
    page.update()

def update_time(page):
    now = datetime.now()
    hora=int(now.strftime("%H"))
    set_stats(page,"tiempo",max(18-hora,0))