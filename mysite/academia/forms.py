from django import forms
from .models import Curso, Idioma, Estudiante, Profesor, Inscripcion, Evaluacion, MaterialDidactico

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

class IdiomaForm(forms.ModelForm):
    class Meta:
        model = Idioma
        fields = '__all__'

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = '__all__'
        widgets = {
            'fecha_finalizacion': forms.DateInput(attrs={'type': 'date'}),
        }

class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = '__all__'
        widgets = {
            'fecha_evaluacion': forms.DateInput(attrs={'type': 'date'}),
        }

class MaterialDidacticoForm(forms.ModelForm):
    class Meta:
        model = MaterialDidactico
        fields = '__all__'
