from django.urls import path
from .views import (
    index,
    curso_list, curso_create, curso_update, curso_delete,
    idioma_list, idioma_create, idioma_update, idioma_delete,
    estudiante_list, estudiante_create, estudiante_update, estudiante_delete,
    profesor_list, profesor_create, profesor_update, profesor_delete,
    inscripcion_list, inscripcion_create, inscripcion_update, inscripcion_delete,
    evaluacion_list, evaluacion_create, evaluacion_update, evaluacion_delete,
    material_didactico_list, material_didactico_create, material_didactico_update, material_didactico_delete
)

app_name = 'academia'  # Añadido para el namespacing

urlpatterns = [
    # Página de inicio
    path('', index, name='index'),

    # Cursos
    path('cursos/', curso_list, name='curso-list'),
    path('cursos/nuevo/', curso_create, name='curso-create'),
    path('cursos/<int:pk>/editar/', curso_update, name='curso-update'),
    path('cursos/<int:pk>/eliminar/', curso_delete, name='curso-delete'),

    # Idiomas
    path('idiomas/', idioma_list, name='idioma-list'),
    path('idiomas/nuevo/', idioma_create, name='idioma-create'),
    path('idiomas/<int:pk>/editar/', idioma_update, name='idioma-update'),
    path('idiomas/<int:pk>/eliminar/', idioma_delete, name='idioma-delete'),

    # Estudiantes
    path('estudiantes/', estudiante_list, name='estudiante-list'),
    path('estudiantes/nuevo/', estudiante_create, name='estudiante-create'),
    path('estudiantes/<int:pk>/editar/', estudiante_update, name='estudiante-update'),
    path('estudiantes/<int:pk>/eliminar/', estudiante_delete, name='estudiante-delete'),

    # Profesores
    path('profesores/', profesor_list, name='profesor-list'),
    path('profesores/nuevo/', profesor_create, name='profesor-create'),
    path('profesores/<int:pk>/editar/', profesor_update, name='profesor-update'),
    path('profesores/<int:pk>/eliminar/', profesor_delete, name='profesor-delete'),

    # Inscripciones
    path('inscripciones/', inscripcion_list, name='inscripcion-list'),
    path('inscripciones/nueva/', inscripcion_create, name='inscripcion-create'),
    path('inscripciones/<int:pk>/editar/', inscripcion_update, name='inscripcion-update'),
    path('inscripciones/<int:pk>/eliminar/', inscripcion_delete, name='inscripcion-delete'),

    # Evaluaciones
    path('evaluaciones/', evaluacion_list, name='evaluacion-list'),
    path('evaluaciones/nueva/', evaluacion_create, name='evaluacion-create'),
    path('evaluaciones/<int:pk>/editar/', evaluacion_update, name='evaluacion-update'),
    path('evaluaciones/<int:pk>/eliminar/', evaluacion_delete, name='evaluacion-delete'),

    # Material Didáctico
    path('material/', material_didactico_list, name='material-didactico-list'),
    path('material/nuevo/', material_didactico_create, name='material-didactico-create'),
    path('material/<int:pk>/editar/', material_didactico_update, name='material-didactico-update'),
    path('material/<int:pk>/eliminar/', material_didactico_delete, name='material-didactico-delete'),
]