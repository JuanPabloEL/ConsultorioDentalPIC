from django.urls import path
from . import views

urlpatterns = [
    path('pacientes/registrar/', views.registrar_paciente, name='registrar_paciente'),
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('citas/agendar/', views.agendar_cita, name='agendar_cita'),
    path('citas/', views.lista_citas, name='lista_citas'),
    path('citas/editar/<int:id>/', views.editar_cita, name='editar_cita'),
    path('citas/cancelar/<int:id>/', views.cancelar_cita, name='cancelar_cita'),
    path('citas/historial/<int:paciente_id>/', views.historial_citas_paciente, name='historial_citas_paciente'),
]