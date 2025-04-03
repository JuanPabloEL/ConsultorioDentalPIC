from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.contrib.auth import get_user_model

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombre, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, nombre=nombre, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, nombre, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, nombre, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    ROLES = [
        ('admin', 'Admin'),
        ('dentista', 'Dentista'),
        ('secretaria', 'Secretaria'),
    ]
    
    
    email = models.EmailField(unique=True)
    nombre = nombre = models.CharField(max_length=150, null=True, blank=True)
    rol = models.CharField(max_length=20, choices=ROLES, default='dentista')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    dentista = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='secretarias')
    

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.email
    
    def is_admin(self):
        return self.rol == 'admin'
    
    def is_dentista(self):
        return self.rol == 'dentista'
    
    def is_secretaria(self):
        return self.rol == 'secretaria'

class PermisoSecretaria(models.Model):
    secretaria = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='permisos')
    Per_crear_cita = models.BooleanField(default=False)
    Per_eliminar_cita = models.BooleanField(default=False)
    Per_ver_cita = models.BooleanField(default=False)
    Per_act_pac = models.BooleanField(default=False)

    def __str__(self):
        return f'Permisos de {self.secretaria.nombre}'