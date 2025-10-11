# Aquí defines las pistas, contraseñas y rutas posibles
LEVELS = {
    "1": {
        "text": "💌 Pista 1:\nEl lugar donde comenzó todo...",
        "password": "cafe",
        "next": ["2A", "2B"],
<<<<<<< HEAD
        "image": "assets/images/portada.png",
=======
        "image": "assets/images/perritos.jpg",
>>>>>>> branch
    },
    "2A": {
        "text": "🌳 Pista 2A:\nBusca el árbol donde oramos juntos por primera vez.",
        "password": "fe",
        "next": ["final"],
<<<<<<< HEAD
        "image": "assets/images/corazon.png",
=======
        "image": "assets/images/corazon.jpg",
>>>>>>> branch
    },
    "2B": {
        "text": "☕ Pista 2B:\nRecuerda aquel café donde te reíste sin parar.",
        "password": "risa",
        "next": ["final"],
        "image": "assets/images/corazon.png",
    },
    "final": {
        "text": "💍 Has completado la carrera del amor. Prepárate para el gran momento.",
        "password": "",
        "next": ["success"],
        "image": "assets/images/corazon.png",
    },
}