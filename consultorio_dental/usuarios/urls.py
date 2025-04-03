from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('agregar-dentista/', views.agregar_dentista, name='agregar_dentista'),
    path('secretarias/', views.lista_secretarias, name='lista_secretarias'),
    path('secretarias/crear/', views.crear_secretaria, name='crear_secretaria'),
    path('secretarias/eliminar/<int:id>/',views.deletesecretaria, name='deletesecretaria'),
    path('secretarias/permisos/<int:id>/', views.asignar_permisos, name='asignar_permisos')
]
