from django.db import models
from django.contrib.auth.models import User


class Funcion(models.Model):
    idfuncion = models.AutoField(primary_key=True)
    idobra = models.IntegerField()
    idsala = models.IntegerField()
    fecha = models.DateField()
    hora = models.TimeField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cupo = models.IntegerField()
    fechaalta = models.DateTimeField()
    fechabaja = models.DateTimeField(null=True, blank=True)
    idestadofuncion = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False  # porque ya existe en Render
        db_table = 'funcion'

    def __str__(self):
        return f"{self.fecha} {self.hora} - Cupo: {self.cupo}"
