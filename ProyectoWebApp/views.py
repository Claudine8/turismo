from django.shortcuts import render, HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from.models import Productos, Categorias

from .forms import CustomUserCreationForm



# Create your views here.

def home(request):
    tres_productos=Productos.objects.all().order_by("-id")[0:3]
    resto_productos = Productos.objects.all().order_by("-id")[3:]
    contexto={
             'tres_productos': tres_productos,
             'resto_productos': resto_productos
            }

    return render(request, "ProyectoWebApp/home.html", contexto)

def categorias(request, categorias_id):
    categoria = Categorias.objects.get(id=categorias_id)
    productos = Productos.objects.filter(categoria=categoria)

    contexto = {
        'productos': productos
    }

    return render(request,"ProyectoWebApp/categorias.html", contexto) 

def acerca(request):

    return render(request, "ProyectoWebApp/acerca.html")

def contacto(request):

    return render(request, "ProyectoWebApp/contacto.html")

def nuevo(request):

    return render(request, "ProyectoWebApp/nuevo.html")

def visualizar(request, id):
    producto = Productos.objects.all().filter(id=id)
    context = {
           'producto': producto
    }
    return render(request, 'ProyectoWebApp/visualizar.html', context)

def registro(request):
    contexto = {
             'form': CustomUserCreationForm()
            }

    if request.method == 'POST':
      formulario = CustomUserCreationForm(data=request.POST)
      if formulario.is_valid():
          formulario.save()
          user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
          login(request, user)
          return redirect(to="HOME")
          contexto["form"] = formulario
    return render(request, 'registration/registro.html', contexto)


#CARRITO
from .carrito import Carrito

def carrito(request):
    return render(request, 'ProyectoWebApp/carrito/carrito.html')



def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id=producto_id)
    carrito.agregar(producto=producto)
    return redirect("carrito")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id=producto_id)
    carrito.eliminar(producto=producto)
    return redirect("carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id=producto_id)
    carrito.restar_producto(producto=producto)
    return redirect("carrito")

def vaciar_carrito(request):
    carrito = Carrito(request)
    carrito.vaciar_carrito()
    return redirect("carrito")