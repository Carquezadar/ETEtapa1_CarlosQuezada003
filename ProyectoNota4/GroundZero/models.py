from django.db import models

# Create your models here.

class Moneda(models.Model):
    idMoneda = models.IntegerField(primary_key=True, verbose_name='Id de moneda')
    nombreMoneda = models.CharField(max_length=50, verbose_name='Nombre de la moneda')

    def __str__(self): 
        return self.nombreMoneda


class Contacto(models.Model):
    NumIdentificaion = models.CharField(max_length=30, primary_key=True, verbose_name='NumIdentificacion')
    imagen = models.ImageField(upload_to='img/', null=True, blank=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre completo')
    telefono = models.CharField(max_length=20, verbose_name='Telefono')
    direccion = models.CharField(max_length=20, verbose_name='direccion')
    email = models.CharField(max_length=50, verbose_name='Email')
    pais = models.CharField(max_length=20, verbose_name='Pais')
    contraseña = models.CharField(max_length=20, verbose_name='Constraseña')
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)

    def __str__(self):
        return self.NumIdentificaion