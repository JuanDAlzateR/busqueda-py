def check_password(level_id, user_input, levels):
    """Verifica si la contraseña es correcta para una pista dada."""
    correct = levels[level_id]["password"].strip().lower()
    return user_input.strip().lower() == correct