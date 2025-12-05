from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Curso, Idioma, Estudiante, Profesor, Inscripcion, Evaluacion, MaterialDidactico
from .forms import CursoForm, IdiomaForm, EstudianteForm, ProfesorForm, InscripcionForm, EvaluacionForm, MaterialDidacticoForm
from django.views.decorators.csrf import ensure_csrf_cookie

# --- Vistas basadas en funciones para la interfaz web ---

# Página de inicio
def index(request):
    cursos = Curso.objects.all()
    estudiantes = Estudiante.objects.all()
    profesores = Profesor.objects.all()
    context = {
        'cursos': cursos,
        'estudiantes': estudiantes,
        'profesores': profesores,
    }
    return render(request, 'index.html', context)

# Vistas para Curso
def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'curso_list.html', {'cursos': cursos})

@ensure_csrf_cookie
def curso_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('academia:curso-list')
    else:
        form = CursoForm()
    return render(request, 'curso_form.html', {'form': form, 'title': 'Añadir Curso'})

@ensure_csrf_cookie
def curso_update(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('academia:curso-list')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'curso_form.html', {'form': form, 'title': 'Editar Curso'})

def curso_delete(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('academia:curso-list')
    return render(request, '_confirm_delete.html', {'object': curso, 'tipo': 'Curso'})

# Vistas para Idioma
def idioma_list(request):
    idiomas = Idioma.objects.all()
    return render(request, 'idioma_list.html', {'idiomas': idiomas})

@ensure_csrf_cookie
def idioma_create(request):
    if request.method == 'POST':
        form = IdiomaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('academia:idioma-list')
    else:
        form = IdiomaForm()
    return render(request, 'idioma_form.html', {'form': form, 'title': 'Añadir Idioma'})

@ensure_csrf_cookie
def idioma_update(request, pk):
    idioma = get_object_or_404(Idioma, pk=pk)
    if request.method == 'POST':
        form = IdiomaForm(request.POST, instance=idioma)
        if form.is_valid():
            form.save()
            return redirect('academia:idioma-list')
    else:
        form = IdiomaForm(instance=idioma)
    return render(request, 'idioma_form.html', {'form': form, 'title': 'Editar Idioma'})

def idioma_delete(request, pk):
    idioma = get_object_or_404(Idioma, pk=pk)
    if request.method == 'POST':
        idioma.delete()
        return redirect('academia:idioma-list')
    return render(request, '_confirm_delete.html', {'object': idioma, 'tipo': 'Idioma'})


# Vistas para Estudiante
def estudiante_list(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiante_list.html', {'estudiantes': estudiantes})

@ensure_csrf_cookie
def estudiante_create(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('academia:estudiante-list')
    else:
        form = EstudianteForm()
    return render(request, 'estudiante_form.html', {'form': form, 'title': 'Añadir Estudiante'})

@ensure_csrf_cookie
def estudiante_update(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('academia:estudiante-list')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'estudiante_form.html', {'form': form, 'title': 'Editar Estudiante'})

def estudiante_delete(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('academia:estudiante-list')
    return render(request, '_confirm_delete.html', {'object': estudiante, 'tipo': 'Estudiante'})


# Vistas para Profesor
def profesor_list(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesor_list.html', {'profesores': profesores})

@ensure_csrf_cookie
def profesor_create(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('academia:profesor-list')
    else:
        form = ProfesorForm()
    return render(request, 'profesor_form.html', {'form': form, 'title': 'Añadir Profesor'})

@ensure_csrf_cookie
def profesor_update(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('academia:profesor-list')
    else:
        form = ProfesorForm(instance=profesor)
    return render(request, 'profesor_form.html', {'form': form, 'title': 'Editar Profesor'})

def profesor_delete(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        profesor.delete()
        return redirect('academia:profesor-list')
    return render(request, '_confirm_delete.html', {'object': profesor, 'tipo': 'Profesor'})

# Vistas para Inscripcion
def inscripcion_list(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'inscripcion_list.html', {'inscripciones': inscripciones})

@ensure_csrf_cookie
def inscripcion_create(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('academia:inscripcion-list')
    else:
        form = InscripcionForm()
    return render(request, 'inscripcion_form.html', {'form': form, 'title': 'Añadir Inscripción'})

@ensure_csrf_cookie
def inscripcion_update(request, pk):
    inscripcion = get_object_or_404(Inscripcion, pk=pk)
    if request.method == 'POST':
        form = InscripcionForm(request.POST, instance=inscripcion)
        if form.is_valid():
            form.save()
            return redirect('academia:inscripcion-list')
    else:
        form = InscripcionForm(instance=inscripcion)
    return render(request, 'inscripcion_form.html', {'form': form, 'title': 'Editar Inscripción'})

def inscripcion_delete(request, pk):
    inscripcion = get_object_or_404(Inscripcion, pk=pk)
    if request.method == 'POST':
        inscripcion.delete()
        return redirect('academia:inscripcion-list')
    return render(request, '_confirm_delete.html', {'object': inscripcion, 'tipo': 'Inscripción'})

# Vistas para Evaluacion
def evaluacion_list(request):
    evaluaciones = Evaluacion.objects.all()
    return render(request, 'evaluacion_list.html', {'evaluaciones': evaluaciones})

@ensure_csrf_cookie
def evaluacion_create(request):
    if request.method == 'POST':
        form = EvaluacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('academia:evaluacion-list')
    else:
        form = EvaluacionForm()
    return render(request, 'evaluacion_form.html', {'form': form, 'title': 'Añadir Evaluación'})

@ensure_csrf_cookie
def evaluacion_update(request, pk):
    evaluacion = get_object_or_404(Evaluacion, pk=pk)
    if request.method == 'POST':
        form = EvaluacionForm(request.POST, instance=evaluacion)
        if form.is_valid():
            form.save()
            return redirect('academia:evaluacion-list')
    else:
        form = EvaluacionForm(instance=evaluacion)
    return render(request, 'evaluacion_form.html', {'form': form, 'title': 'Editar Evaluación'})

def evaluacion_delete(request, pk):
    evaluacion = get_object_or_404(Evaluacion, pk=pk)
    if request.method == 'POST':
        evaluacion.delete()
        return redirect('academia:evaluacion-list')
    return render(request, '_confirm_delete.html', {'object': evaluacion, 'tipo': 'Evaluación'})

# Vistas para MaterialDidactico
def material_didactico_list(request):
    materiales = MaterialDidactico.objects.all()
    return render(request, 'material_didactico_list.html', {'materiales': materiales})

@ensure_csrf_cookie
def material_didactico_create(request):
    if request.method == 'POST':
        form = MaterialDidacticoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('academia:material-didactico-list')
    else:
        form = MaterialDidacticoForm()
    return render(request, 'material_didactico_form.html', {'form': form, 'title': 'Añadir Material Didáctico'})

@ensure_csrf_cookie
def material_didactico_update(request, pk):
    material = get_object_or_404(MaterialDidactico, pk=pk)
    if request.method == 'POST':
        form = MaterialDidacticoForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('academia:material-didactico-list')
    else:
        form = MaterialDidacticoForm(instance=material)
    return render(request, 'material_didactico_form.html', {'form': form, 'title': 'Editar Material Didáctico'})

def material_didactico_delete(request, pk):
    material = get_object_or_404(MaterialDidactico, pk=pk)
    if request.method == 'POST':
        material.delete()
        return redirect('academia:material-didactico-list')
    return render(request, '_confirm_delete.html', {'object': material, 'tipo': 'Material Didáctico'})
