from django.contrib import admin
from .models import Idioma, Curso, Estudiante, Profesor, Inscripcion, Evaluacion, MaterialDidactico

@admin.register(Idioma)
class IdiomaAdmin(admin.ModelAdmin):
    list_display = ('nombre_idioma',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre_curso', 'idioma', 'nivel', 'profesor_asignado', 'fecha_inicio', 'fecha_fin')
    list_filter = ('idioma', 'nivel', 'profesor_asignado')
    search_fields = ('nombre_curso', 'descripcion')

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre_estudiante', 'apellido_estudiante', 'email', 'fecha_nacimiento')
    search_fields = ('nombre_estudiante', 'apellido_estudiante', 'email')

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre_profesor', 'apellido_profesor', 'email', 'especialidad')
    list_filter = ('especialidad',)
    search_fields = ('nombre_profesor', 'apellido_profesor', 'email')

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'curso', 'fecha_inscripcion', 'estado')
    list_filter = ('curso', 'estado')
    search_fields = ('estudiante__nombre_estudiante', 'curso__nombre_curso')

@admin.register(Evaluacion)
class EvaluacionAdmin(admin.ModelAdmin):
    list_display = ('inscripcion', 'fecha_evaluacion', 'calificacion')
    list_filter = ('inscripcion__curso',)
    search_fields = ('inscripcion__estudiante__nombre_estudiante', 'inscripcion__curso__nombre_curso')

@admin.register(MaterialDidactico)
class MaterialDidacticoAdmin(admin.ModelAdmin):
    list_display = ('nombre_material', 'curso', 'tipo_material', 'costo', 'es_obligatorio')
    list_filter = ('tipo_material', 'es_obligatorio', 'curso')
    search_fields = ('nombre_material', 'descripcion')
