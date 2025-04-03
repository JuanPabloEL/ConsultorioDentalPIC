from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

@csrf_exempt
@login_required
def agregar_dentista(request):
    if not request.user.is_superuser:
        return JsonResponse({'error':'No tienes permisos para realizar esta accion'}, status=403)
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            nombre = data.get('nombre')
            password = data.get('password')

            if not (email and nombre and password): 
                return JsonResponse({'error': 'Email, nombre y contraseña son requeridos'}, status=400)

            dentista = User.objects.create_user(email=email, nombre=nombre, password=password, rol = 'dentista')
            return JsonResponse({'message': 'Dentista agregado exitosamente', 'dentista': dentista.email})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
    return JsonResponse({'error': 'Método no permitido'}, status=405)