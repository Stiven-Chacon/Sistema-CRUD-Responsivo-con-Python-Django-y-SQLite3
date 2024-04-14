from django.db import models

# Modelo de la base de datos
class Curso(models.Model):
    cogido=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=50)
    credito=models.PositiveBigIntegerField()#Es un campo de entero pequeño

    def __str__(self):
        Texto = "{0} ({1})"
        return Texto.format(self.nombre, self.credito)