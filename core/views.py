from django.shortcuts import render, redirect
from .models import Paciente, Cita, Doctor
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Sintoma, Enfermedad, Tratamiento, Doctor, Paciente, Prescripcion
from .forms import SintomaForm




def inicio_view(request):
    return render(request, 'core/inicio.html')
def contactos_view(request):
       return render(request, 'core/contactos.html')  # Asegúrate de tener este archivo
# views.py
@login_required
def dashboard_doctor(request):
    citas = Cita.objects.filter(doctor=request.user.doctor).order_by('fecha_hora')[:5]
    pacientes_recientes = Paciente.objects.filter(cita__doctor=request.user.doctor).distinct()[:10]
    return render(request, 'core/dashboard_doctor.html', {
        'citas': citas,
        'pacientes_recientes': pacientes_recientes,
    })

@login_required
def dashboard_paciente(request):
    paciente = Paciente.objects.get(user=request.user)
    tratamientos = Tratamiento.objects.filter(paciente=paciente)
    citas = Cita.objects.filter(paciente=paciente)  # Obtener citas del paciente
    return render(request, 'core/dashboard_paciente.html', {
        'paciente': paciente,
        'tratamientos': tratamientos,
        'citas': citas,  # Pasar citas al contexto
    })


def pacientes(request):
    pacientes = Paciente.objects.all().order_by('-ultima_actividad')
    return render(request, 'core/pacientes.html', {
        'pacientes': pacientes,
    })
def lista_pacientes(request):
    # Obtener todos los pacientes
    pacientes = Paciente.objects.all()

    # Aplicar filtros si existen
    enfermedad = request.GET.get('enfermedad')
    if enfermedad:
        pacientes = pacientes.filter(detalles__icontains=enfermedad)

    return render(request, 'core/pacientes.html', {'pacientes': pacientes})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_pacientes')  # Redirige al listado
        else:
            return render(request, 'core/login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'core/login.html')

def agregar_paciente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        detalles = request.POST['detalles']
        
        # Crear el paciente
        paciente = Paciente.objects.create(
            nombre=nombre,
            fecha_nacimiento=fecha_nacimiento,
            detalles=detalles,
            user=request.user  # Asegúrate de asociar el paciente con el usuario
        )
        
        return redirect('lista_pacientes')  # Redirigir a la lista de pacientes
    return render(request, 'core/agregar_paciente.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'core/register.html', {'error': 'El usuario ya existe'})
        user = User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'core/register.html')

def lista_doctores(request):
    doctores = Doctor.objects.all()  # Asegúrate de que esto esté correcto
    return render(request, 'core/doctores.html', {'doctores': doctores})

def prescripcion_view(request):
    if request.method == 'POST':
        # Lógica para manejar la prescripción
        pass
    return render(request, 'core/prescripcion.html')

def doctores_view(request):
       doctores = Doctor.objects.all()  # Obtener todos los doctores
       return render(request, 'core/doctores.html', {'doctores': doctores})

def servicios_view(request):
    return render(request, 'core/servicios.html')

def registrar_sintomas(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == "POST":
        sintomas = request.POST.get('sintomas')
        # Lógica para guardar los síntomas
        # Por ejemplo, guardar en un modelo relacionado
        paciente.detalles += f"\nSíntomas registrados: {sintomas}"
        paciente.save()
        return redirect('lista_pacientes')
    return render(request, 'core/registrar_sintomas.html', {'paciente': paciente})

def registrar_sintomas_general(request):
    if request.method == "POST":
        sintomas = request.POST.get('sintomas')
        # Lógica para manejar los síntomas generales
        # Por ejemplo, agregar un registro global
        return redirect('lista_pacientes')
    return render(request, 'core/registrar_sintomas_general.html')