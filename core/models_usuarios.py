from django.db import models

class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=150)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    rol = models.CharField(max_length=20)
    fechaalta = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False  
        db_table = 'usuario'
