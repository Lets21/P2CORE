from django import forms
from .models import Sintoma, Paciente

class SintomaForm(forms.ModelForm):
    class Meta:
        model = Sintoma
        fields = ['descripcion']
        widgets = {
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Describe tus síntomas'
            }),
        }

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'fecha_nacimiento', 'detalles']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'detalles': forms.Textarea(attrs={'class': 'form-control'}),
        }
