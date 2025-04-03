from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import get_user_model

User = get_user_model()

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return JsonResponse({'error': 'Email y contraseña son obligatorios'}, status=400)


        user = User.objects.get(email=email)
        if user.check_password(password):
            login(request,user)
            return JsonResponse({
                    'message': 'Login Exitoso',
                    'rol': user.rol  # Enviamos el rol del usuario
                })
        else:
            return JsonResponse({'error' : 'Credenciales Invalidas' }, status = 400)
    return JsonResponse({'error' : 'Metodo no permitido' }, status = 400)
        
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({'message': 'Logout exitoso'})
    return JsonResponse({'error': 'No hay usuario autenticado'}, status=400)
