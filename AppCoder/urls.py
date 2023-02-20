from django.urls import path
from AppCoder import views

urlpatterns = [
    
    path('', views.Inicio, name='inicio'),
    path('contacto/', views.ContactoView, name='contacto'),
    path('tienda/', views.Tienda, name='tienda'),
    path('registro/', views.RegistroView, name='registro'),
    path('productosForm/', views.productosForm, name='productosForm'),
    path('envioCorrecto/', views.envioCorrecto, name='envioCorrecto'),
    path('busquedaProductos/', views.busquedaProductos, name='busquedaProductos'),
    path('busquedaProductos/buscar/', views.buscar, name='buscar'),
    
    
    
    
]
