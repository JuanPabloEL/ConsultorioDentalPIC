from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required
from .models import Paciente, Citas
from django.utils.timezone import now

@csrf_exempt
@login_required
def registrar_paciente(request):
    if request.method == 'POST':
        if request.user.rol != 'dentista':
            return JsonResponse({'error': 'No tienes los permisos para registrar pacientes'}, status = 403)
        
        data = json.loads(request.body.decode('utf-8'))
        nombre = data.get('nombre')
        email = data.get('email')
        telefono = data.get('telefono', '')
        direccion =  data.get('direccion', '')

        if Paciente.objects.filter(email=email).exists():
            return JsonResponse({'error' : 'El correo ya esta registrado'}, status = 400)
        
        pacientes = Paciente.objects.create(
            nombre=nombre, email=email, telefono=telefono, direccion=direccion, dentista = request.user
        )
        return JsonResponse({'message' : 'Paciente Registrado existosamente', 'id' : pacientes.id})
    
    return JsonResponse({'error': 'Metodo no permitido'}, status = 405)

@login_required
def lista_pacientes(request):
    if request.user.rol != 'dentista':
        return JsonResponse({'error': 'No tienen permiso para ver pacientes'})
    
    pacientes = Paciente.objects.filter(dentista = request.user)
    data = [{'id': p.id, 'nombre': p.nombre, 'email': p.email, 'direccion': p.direccion} for p in pacientes]
    return JsonResponse({'Pacientes': data})

@csrf_exempt
@login_required
def agendar_cita(request):
    if request.method == 'POST':
        if request.user.rol not in ['dentista', 'secretaria']:
            return JsonResponse({'error': 'No tienes permisos para agendar citas'}, status = 403)
        
        data = json.loads(request.body.decode('utf-8'))
        paciente_id = data.get('paciente_id')
        fecha_hora = data.get('fecha_hora')
        motivo = data.get('motivo')
#        print(paciente_id)
        paciente = get_object_or_404(Paciente, id=paciente_id, dentista = request.user.dentista if request.user.rol == 'secretaria' else request.user)

        cita = Citas.objects.create(
            paciente = paciente,
            dentista = paciente.dentista,
            fecha_hora = fecha_hora,
            motivo = motivo,
            creada_por_secretaria = (request.user.rol == 'secretaria')
        )
        return JsonResponse({'message': 'Cita agendada', 'id': cita.id})
    
    return JsonResponse({'error': 'Metodo no permitido'}, status=405)

@login_required
def lista_citas(request):
    if (request.user.rol == 'dentista'):
        citas = Citas.objects.filter(dentista=request.user)
    elif (request.user.rol == 'secretaria'):
        citas = Citas.objects.filter(dentista=request.user.dentista)
    else:
        return JsonResponse({'error': 'No tienes permiso para ver citas'}, status=403)
    data = [{'id': c.id, 'paciente': c.paciente.nombre, 'fecha_hora': c.fecha_hora, 'motivo': c.motivo} for c in citas]

    return JsonResponse({'citas': data})

@csrf_exempt
@login_required
def editar_cita(request, id):
    cita = get_object_or_404(Citas, id=id)

    if request.user.rol not in ['dentista', 'secretaria']:
        return JsonResponse({'error': 'No tienes permiso para editar esta cita'}, status=403)
    
    if request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        cita.fecha_hora = data.get('fecha_hora', cita.fecha_hora)
        cita.motivo = data.get('motivo', cita.motivo)
        cita.save()
        return JsonResponse({'message': 'La cita ha sido actualizada'})
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
@login_required
def cancelar_cita(request, id):
    cita = get_object_or_404(Citas, id=id)

    if request.user.rol not in ['dentista', 'secretaria']:
        return JsonResponse({'error': 'No tienes permiso para cancelar la cita'}, status=403)
    
    if request.method == 'DELETE':
        cita.delete()
        return JsonResponse({'message': 'Cita cancelada correctamente'})
    
    return JsonResponse({'error': 'Metodo no permitido'}, status = 405)

@login_required
def historial_citas_paciente(request, paciente_id):
    # Verifica si el usuario es un dentista
    if request.user.rol != 'dentista':
        return JsonResponse({'error': 'No tienes permiso para ver el historial de ese paciente'})
    
    paciente = get_object_or_404(Paciente, id=paciente_id, dentista= request.user)

    citas = Citas.objects.filter(paciente=paciente).order_by('-fecha_hora')

    data = [
        {
            'id': c.id,
            'fecha_hora': c.fecha_hora,
            'motivo': c.motivo
        }
        for c in citas
    ]

    return JsonResponse({'Historial_citas': data})