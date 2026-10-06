from django.shortcuts import render

TEMAS_DATA = {
    1: {
        'id': 1,
        'titulo': 'Tema 1: Arquitectura MVT en Django',
        'descripcion': 'Explicación del funcionamiento de Modelos, Vistas y Templates en el desarrollo web.',
        'imagenes': ['images/tema1_img1.jpg', 'images/tema1_img2.jpeg']
    },
    2: {
        'id': 2,
        'titulo': 'Tema 2: Control de Versiones con Git y GitHub',
        'descripcion': 'Uso de comandos de Git, repositorios remotos y gestión de cambios de código.',
        'imagenes': ['images/tema2_img1.jpeg', 'images/tema2_img2.png']
    }
}

def home(request):
    contexto = {
        'temas': list(TEMAS_DATA.values())
    }
    return render(request, 'inicio/inicio.html', contexto)


def detalle_tema(request, tema_id):
    tema = TEMAS_DATA.get(tema_id)
    return render(request, 'inicio/detalle.html', {'tema': tema})