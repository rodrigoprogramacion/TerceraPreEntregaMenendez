from django.shortcuts import render,HttpResponse
from AppCoder.models import *
from AppCoder.forms import *

# Create your views here.


def Inicio(request):
    return render(request, 'AppCoder/inicio.html')


def Tienda(request):
    return render(request, 'AppCoder/tienda.html')


def envioCorrecto(request):
    return render(request, 'AppCoder/envioCorrecto.html')

def busquedaProductos(request):
    return render(request, 'AppCoder/busquedaproductos.html')


def productosForm(request):
    if request.method == 'POST':
        miFormulario = ProductosForm(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            producto = Ecommerce(
                nombreProducto=informacion['nombreProducto'], codigoProducto=informacion['codigoProducto'], precioProducto=informacion['precioProducto'])
            producto.save()
            return render(request, 'AppCoder/envioCorrecto.html')
    else:
        miFormulario = ProductosForm()

    return render(request, 'AppCoder/productosForm.html', {"miFormulario": miFormulario})


def RegistroView(request):
    if request.method == 'POST':
        miFormularioRegistro = RegistroForm(request.POST)
        print(miFormularioRegistro)

        if miFormularioRegistro.is_valid:
            informacionRegistro = miFormularioRegistro.cleaned_data
            usuarioR = Registro(
                usuario=informacionRegistro['usuarioRegistro'], password=informacionRegistro['passwordRegistro'], email=informacionRegistro['emailRegistro'])
            usuarioR.save()
            return render(request, 'AppCoder/envioCorrecto.html')
    else:
        miFormularioRegistro = RegistroForm()

    return render(request, 'AppCoder/registro.html', {"miFormularioRegistro": miFormularioRegistro})

def ContactoView(request):
    if request.method == 'POST':
        miFormularioContacto = ContactoForm(request.POST)
        print(miFormularioContacto)

        if miFormularioContacto.is_valid:
            informacionContacto = miFormularioContacto.cleaned_data
            usuarioC = Contacto(
               nombreContacto=informacionContacto['nombreContacto'], emailContacto=informacionContacto['emailContacto'], mensajeContacto=informacionContacto['mensajeContacto'])
            usuarioC.save()
            return render(request, 'AppCoder/inicio.html',)
    else:
        miFormularioContacto = ContactoForm()

    return render(request, 'AppCoder/contacto.html', {"miFormularioContacto": miFormularioContacto})


def buscar(request):

    if request.GET["prd"]:

        #mensaje="Articulo buscado: %r" %request.GET["prd"]
        producto=request.GET["prd"]

        articulos=Ecommerce.objects.filter(nombreProducto__icontains=producto)

        return render(request,"AppCoder/resultadoBusqueda.html",{"articulos":articulos, "query":producto})
    else:

        mensaje="No has introducido nada!"

    return HttpResponse(mensaje)
