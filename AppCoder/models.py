from django.db import models

# Create your models here.
class Registro(models.Model):
    usuario=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=60)

    def __str__(self):
        return f"Usuario: {self.usuario} - Email {self.email}"

class Ecommerce(models.Model):
    nombreProducto=models.CharField(max_length=50)
    codigoProducto=models.CharField(max_length=50)
    precioProducto=models.CharField(max_length=60)

    def __str__(self):
        return f"Nombre: {self.nombreProducto} - Precio {self.precioProducto}"

class Contacto(models.Model):
    nombreContacto=models.CharField(max_length=50)
    emailContacto=models.CharField(max_length=50)
    mensajeContacto=models.CharField(max_length=250)
    
    def __str__(self):
        return f"Nombre: {self.nombreContacto} - Email {self.emailContacto} - Precio {self.mensajeContacto}"