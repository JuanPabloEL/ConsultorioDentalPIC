from .views.auth import login_view, logout_view
from .views.admin import agregar_dentista
from .views.dentista import lista_secretarias, crear_secretaria, deletesecretaria, asignar_permisos

__all__ = [
    "login_view",
    "logout_view",
    "agregar_dentista",
    "lista_secretarias",
    "crear_secretaria",
    "deletesecretaria",
    "asignar_permisos"
]
