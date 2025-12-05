from django.db import models

class Idioma(models.Model):
    nombre_idioma = models.CharField(max_length=100, unique=True, help_text="Nombre del idioma (ej. Inglés, Francés)")

    def __str__(self):
        return self.nombre_idioma

class Curso(models.Model):
    nombre_curso = models.CharField(max_length=200, help_text="Nombre del curso")
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE, related_name="cursos")
    nivel = models.CharField(max_length=50, help_text="Nivel del curso (ej. A1, B2, Avanzado)")
    descripcion = models.TextField(blank=True, null=True, help_text="Descripción detallada del curso")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    profesor_asignado = models.ForeignKey('Profesor', on_delete=models.SET_NULL, null=True, blank=True, related_name="cursos_impartidos")
    horario = models.CharField(max_length=100, help_text="Horario del curso (ej. L-V 10:00-12:00)")
    capacidad_maxima = models.PositiveIntegerField(default=20)

    def __str__(self):
        return f"{self.nombre_curso} ({self.idioma.nombre_idioma})"

class Estudiante(models.Model):
    nombre_estudiante = models.CharField(max_length=100)
    apellido_estudiante = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_estudiante} {self.apellido_estudiante}"

class Profesor(models.Model):
    nombre_profesor = models.CharField(max_length=100)
    apellido_profesor = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    especialidad = models.ForeignKey(Idioma, on_delete=models.SET_NULL, null=True, blank=True)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_profesor} {self.apellido_profesor}"

class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="inscripciones")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="inscripciones")
    fecha_inscripcion = models.DateField(auto_now_add=True)
    ESTADO_CHOICES = (
        ('activa', 'Activa'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    )
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activa')

    def __str__(self):
        return f"{self.estudiante} inscrito en {self.curso}"

class Evaluacion(models.Model):
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE, related_name="evaluaciones")
    fecha_evaluacion = models.DateField()
    calificacion = models.DecimalField(max_digits=5, decimal_places=2, help_text="Calificación de 0 a 100")
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Evaluación de {self.inscripcion.estudiante} en {self.inscripcion.curso}"

class MaterialDidactico(models.Model):
    nombre_material = models.CharField(max_length=200)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='materiales')
    TIPO_CHOICES = (
        ('libro', 'Libro de Texto'),
        ('guia', 'Guía de Ejercicios'),
        ('digital', 'Recurso Digital'),
        ('otro', 'Otro'),
    )
    tipo_material = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descripcion = models.TextField(blank=True, null=True)
    costo = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    editorial = models.CharField(max_length=100, blank=True, null=True)
    es_obligatorio = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre_material} para el curso {self.curso.nombre_curso}"
