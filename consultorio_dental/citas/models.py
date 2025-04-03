from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL  

class Paciente(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    dentista = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pacientes")

    def __str__(self):
        return f"{self.nombre} - {self.email}"
    
class Citas(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="citas")
    dentista = models.ForeignKey(User, on_delete=models.CASCADE, related_name="citas_dentista")
    fecha_hora = models.DateTimeField()
    motivo = models.TextField()
    creada_por_secretaria = models.BooleanField(default=False)

    def __str__(self):
        return f'Cita de {self.paciente.nombre} con {self.dentista.nombre} el {self.fecha_hora}'