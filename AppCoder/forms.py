from django import forms

class ProductosForm(forms.Form):
    nombreProducto = forms.CharField(label="Nombre del producto")
    codigoProducto = forms.CharField(label="Codigo del producto")
    precioProducto = forms.CharField(label="Precio del producto")

class RegistroForm(forms.Form):
    usuarioRegistro = forms.CharField(label="Usuario")
    passwordRegistro = forms.CharField(label="Password", widget=forms.PasswordInput)
    emailRegistro=forms.CharField(label="Email")
   
class ContactoForm(forms.Form):
    nombreContacto = forms.CharField(label="Nombre")
    emailContacto = forms.CharField(label="Email")
    mensajeContacto = forms.CharField(label="Mensaje")