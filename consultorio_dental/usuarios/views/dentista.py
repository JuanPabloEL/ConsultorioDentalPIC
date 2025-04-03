from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from ..models import PermisoSecretaria

User = get_user_model()

@login_required
def lista_secretarias(request):
    if request.user.rol != 'dentista':
        raise PermissionDenied("Solo los dentistas pueden ver a sus secretarias")
    
    secretarias = User.objects.filter(rol = 'secretaria', dentista= request.user)
    data = [{'id': s.id, 'nombre': s.nombre, 'email': s.email} for s in secretarias]
    return JsonResponse({'secretarias': data})

@csrf_exempt
@login_required
def crear_secretaria(request):
    if (request.method == 'POST' and request.user.rol == 'dentista'):
        data = json.loads(request.body.decode('utf-8'))
        nombre = data.get('nombre')
        email = data.get('email')
        password = data.get('password')

        if User.objects.filter(email=email).exists():
            return JsonResponse({'error' : 'El correo ya esta en uso'}, status = 400)
        
        secretaria = User.objects.create_user(
            email=email,
            nombre=nombre,
            password=password,
            rol = 'secretaria',
            dentista = request.user
        )

        return JsonResponse({'mensaje' : 'Secretaria registrada con exito', 'id': secretaria.id})
    
    return JsonResponse({'error': 'Método no permitido'}, status = 405)

@csrf_exempt
@login_required
def deletesecretaria(request, id):
    if request.method == 'DELETE':
        if request.user.rol != 'dentista':
            return JsonResponse({'error': 'No tienes permisos para eliminar secretarias'}, status=403)
        
        try:
            secretaria = User.objects.get(id=id, dentista=request.user)
            secretaria.delete()
            return JsonResponse({'message': 'Secretaria eliminada exitosamente'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'Secretaria no encontrada'}, status=404)

    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
@login_required
def asignar_permisos(request, id):
    if request.method == 'POST':
        if request.user.rol != 'dentista':
            return JsonResponse({'error': 'No tienes permisos para asignar permisos'}, status=403)
        
        try:
            secretaria = User.objects.get(id=id, rol = 'secretaria', dentista = request.user)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Secretaria no encontrada o no autorizada'}, status=404)
        data = json.loads(request.body.decode('utf-8'))

        permisos, created = PermisoSecretaria.objects.get_or_create(secretaria=secretaria)
        permisos.Per_ver_cita = data.get('Per_ver_cita', permisos.Per_ver_cita)
        permisos.Per_crear_cita = data.get('Per_crear_cita', permisos.Per_crear_cita)
        permisos.Per_eliminar_cita = data.get('Per_eliminar_cita', permisos.Per_eliminar_cita)
        permisos.Per_act_pac = data.get('Per_act_pac', permisos.Per_act_pac)
        permisos.save()

        return JsonResponse({'message': 'Permisos actualizados correctamente'})

    return JsonResponse({'error': 'Método no permitido'}, status=405)