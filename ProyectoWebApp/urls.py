from django.urls import path

from ProyectoWebApp import views

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="HOME"),
    path('categorias/<categorias_id>/',views.categorias, name="CATEGORIAS"),
    path('acerca/',views.acerca, name="ACERCA DE..."),
    path('contacto/',views.contacto, name="CONTACTO"),
    path('nuevo/',views.nuevo, name="NUEVO PRODUCTO"), 
    path('visualizar/<id>',views.visualizar, name="VISUALIZAR"),
    path('registro/', views.registro, name="REGISTRO"),
    path('agregar/', views.agregar_producto, name='carrito'),
    path('carrito/', views.carrito, name='carrito'),
    path('agregar/<producto_id>/', views.agregar_producto, name='agregar_producto'),
    path('eliminar/<producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('restar/<producto_id>/', views.restar_producto, name='restar_producto'),
    path('vaciar/', views.vaciar_carrito, name='vaciar_carrito'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   
