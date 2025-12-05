
from django.core.management.base import BaseCommand
from academia.models import Idioma, Estudiante, Profesor

class Command(BaseCommand):
    help = 'Seeds the database with initial data for Idiomas, Estudiantes, and Profesores'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting to seed initial data...")

        # Seed Idiomas
        self.stdout.write("Seeding Idiomas...")
        idiomas = [
            Idioma(nombre_idioma='Inglés'),
            Idioma(nombre_idioma='Francés'),
            Idioma(nombre_idioma='Alemán'),
            Idioma(nombre_idioma='Español'),
        ]
        Idioma.objects.bulk_create(idiomas, ignore_conflicts=True)
        self.stdout.write(self.style.SUCCESS('Successfully seeded Idiomas.'))

        # Seed Estudiantes
        self.stdout.write("Seeding Estudiantes...")
        estudiantes = [
            Estudiante(nombre_estudiante='Juan', apellido_estudiante='Pérez', email='juan.perez@example.com', fecha_nacimiento='2000-01-15'),
            Estudiante(nombre_estudiante='Ana', apellido_estudiante='García', email='ana.garcia@example.com', fecha_nacimiento='1999-05-20'),
            Estudiante(nombre_estudiante='Carlos', apellido_estudiante='López', email='carlos.lopez@example.com', fecha_nacimiento='2001-09-10'),
        ]
        Estudiante.objects.bulk_create(estudiantes, ignore_conflicts=True)
        self.stdout.write(self.style.SUCCESS('Successfully seeded Estudiantes.'))

        # Seed Profesores
        self.stdout.write("Seeding Profesores...")
        profesores = [
            Profesor(nombre_profesor='Laura', apellido_profesor='Martínez', email='laura.martinez@example.com'),
            Profesor(nombre_profesor='Pedro', apellido_profesor='Sánchez', email='pedro.sanchez@example.com'),
        ]
        Profesor.objects.bulk_create(profesores, ignore_conflicts=True)
        # Assign especialidad to Profesores
        profesor1 = Profesor.objects.get(email='laura.martinez@example.com')
        profesor1.especialidad = Idioma.objects.get(nombre_idioma='Inglés')
        profesor1.save()

        profesor2 = Profesor.objects.get(email='pedro.sanchez@example.com')
        profesor2.especialidad = Idioma.objects.get(nombre_idioma='Francés')
        profesor2.save()
        self.stdout.write(self.style.SUCCESS('Successfully seeded Profesores.'))

        self.stdout.write(self.style.SUCCESS('Initial data seeding complete!'))
