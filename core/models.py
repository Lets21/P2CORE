from django.db import models
from django.contrib.auth.models import User

# Modelo de Doctor
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    especialidad = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos_doctores/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.especialidad}"

# Modelo de Paciente
class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    detalles = models.TextField()

    def __str__(self):
        return self.nombre

# Modelo de Enfermedad
class Enfermedad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    medicos = models.ManyToManyField(Doctor, related_name="enfermedades_capacitadas")  # Médicos capacitados

    def __str__(self):
        return self.nombre

# Modelo de Síntomas
class Sintoma(models.Model):
    descripcion = models.CharField(max_length=255)
    enfermedades = models.ManyToManyField(Enfermedad, related_name="sintomas_relacionados")  # Relación con enfermedades

    def __str__(self):
        return self.descripcion

# Modelo de Tratamiento
class Tratamiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    efectos_secundarios = models.TextField(blank=True, null=True)
    enfermedad = models.CharField(max_length=100, default='Sin enfermedad')

    def __str__(self):
        return f"{self.nombre} - {self.enfermedad}"

# Modelo de Prescripción
class Prescripcion(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="prescripciones")
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE, related_name="prescripciones")
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_fin = models.DateField(null=True, blank=True)
    estado = models.CharField(
        max_length=50,
        choices=[("Pendiente", "Pendiente"), ("En Progreso", "En Progreso"), ("Finalizado", "Finalizado")],
        default="Pendiente"
    )

    def __str__(self):
        return f"Prescripción para {self.paciente.nombre}: {self.tratamiento.nombre}"

# Modelo de Cita
class Cita(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()

    def __str__(self):
        return f"Cita: {self.paciente.nombre} con {self.doctor.user.first_name} {self.doctor.user.last_name}"