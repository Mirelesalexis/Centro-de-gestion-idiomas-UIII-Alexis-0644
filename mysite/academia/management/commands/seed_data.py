
import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from academia.models import Idioma, Curso, Estudiante, Profesor, Inscripcion, Evaluacion, MaterialDidactico

class Command(BaseCommand):
    help = 'Seeds the database with initial data for Cursos, Inscripciones, Evaluaciones, and MaterialDidactico'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting to seed the database...")

        # Get existing data
        idiomas = list(Idioma.objects.all())
        estudiantes = list(Estudiante.objects.all())
        profesores = list(Profesor.objects.all())

        if not all([idiomas, estudiantes, profesores]):
            self.stdout.write(self.style.ERROR('Please ensure there are Idiomas, Estudiantes, and Profesores in the database before running this command.'))
            return

        # Seed Cursos
        self.stdout.write("Seeding Cursos...")
        cursos = []
        for i in range(5):
            idioma = random.choice(idiomas)
            profesor = random.choice(profesores)
            curso = Curso.objects.create(
                nombre_curso=f'Curso de {idioma.nombre_idioma} Nivel {i+1}',
                idioma=idioma,
                nivel=random.choice(['A1', 'A2', 'B1', 'B2', 'C1']),
                descripcion=f'Descripción detallada del curso de {idioma.nombre_idioma}.',
                fecha_inicio=timezone.now().date(),
                fecha_fin=timezone.now().date() + timedelta(days=90),
                profesor_asignado=profesor,
                horario='L-V 10:00-12:00',
                capacidad_maxima=random.randint(15, 25)
            )
            cursos.append(curso)
        self.stdout.write(self.style.SUCCESS('Successfully seeded Cursos.'))

        # Seed Inscripciones
        self.stdout.write("Seeding Inscripciones...")
        inscripciones = []
        for estudiante in estudiantes:
            curso = random.choice(cursos)
            inscripcion, created = Inscripcion.objects.get_or_create(
                estudiante=estudiante,
                curso=curso,
                defaults={'estado': random.choice(['activa', 'completada', 'cancelada'])}            )
            if created:
                inscripciones.append(inscripcion)
        self.stdout.write(self.style.SUCCESS('Successfully seeded Inscripciones.'))

        # Seed Evaluaciones
        self.stdout.write("Seeding Evaluaciones...")
        for inscripcion in inscripciones:
            if inscripcion.estado == 'activa' or inscripcion.estado == 'completada':
                Evaluacion.objects.create(
                    inscripcion=inscripcion,
                    fecha_evaluacion=inscripcion.curso.fecha_fin - timedelta(days=10),
                    calificacion=random.uniform(60, 100),
                    comentarios='Evaluación de fin de curso.'
                )
        self.stdout.write(self.style.SUCCESS('Successfully seeded Evaluaciones.'))

        # Seed MaterialDidactico
        self.stdout.write("Seeding MaterialDidactico...")
        for curso in cursos:
            MaterialDidactico.objects.create(
                nombre_material=f'Libro de Texto para {curso.nombre_curso}',
                curso=curso,
                tipo_material='libro',
                costo=random.uniform(20, 50)
            )
            MaterialDidactico.objects.create(
                nombre_material=f'Guía de Ejercicios para {curso.nombre_curso}',
                curso=curso,
                tipo_material='guia',
                costo=random.uniform(10, 25)
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded MaterialDidactico.'))

        self.stdout.write(self.style.SUCCESS('Database seeding complete!'))
