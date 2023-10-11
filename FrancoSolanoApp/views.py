from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.urls import reverse_lazy
from FrancoSolanoApp.models import *
from FrancoSolanoApp.forms import VendedorFormulario, VentaFormulario, ClienteFormulario, UserEditForm, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

def vendedores(request):
    return render(request, "vendedores.html")

def pages(request):
    return render(request, "pages.html")

def about(request):
    return render(request, "about.html")

# Agregar vendedor
def vendedores_formulario(request):
    if request.method == 'POST':

        FormVendedor = VendedorFormulario(request.POST)

        print(FormVendedor)

        if FormVendedor.is_valid:

            informacion = FormVendedor.cleaned_data

            vendedor_1 = vendedor(nombre=informacion['nombreVendedor'], apellido=informacion['apellidoVendedor'], numero_empleado=informacion['documentoVendedor']) 
            vendedor_1.save()
            print(vendedor_1)
            return render(request, "vendedores.html") 

      
    return render(request, "vendedores_formulario.html")

# Agregar venta
def venta_formulario(request):
    if request.method == 'POST':

        FormVenta = VentaFormulario(request.POST)

        print(FormVenta)

        if FormVenta.is_valid:

            informacion = FormVenta.cleaned_data

            venta_1= venta(fecha=informacion['fechaVenta'], monto=informacion['montoVenta'], numero_vendedor=informacion['documentoVendedor']) 
            venta_1.save()
            
            return render(request, "inicio.html") 

      
    return render(request, "ventas_formulario.html")

# Agregar cliente
def cliente_formulario(request):
    if request.method == 'POST':

        FormCliente = ClienteFormulario(request.POST)

        print(FormCliente)

        if FormCliente.is_valid:

            informacion = FormCliente.cleaned_data

            venta_1= cliente(nombre=informacion['nombreCliente'], apellid=informacion['apellidoCliente'], numero_cliente=informacion['numeroCliente']) 
            venta_1.save()
            
            return render(request, "inicio.html") 

      
    return render(request, "clientes_formulario.html")

def buscar_ventas(request):

    return render(request, "buscar_ventas.html")

def buscar(request):
    if request.GET['documento']:
        id_vendedor = request.GET['documento']
        ventas = venta.objects.filter(numero_vendedor__icontains=id_vendedor)
        return render(request,'vendedores.html',{'Numero vendedor':id_vendedor,'ventas':ventas})
    else:
        return HttpResponse("No hay datos")

    

# Vista de editar el perfil
def editarPerfil(request):
    usuario = request.user


    if request.method == 'POST':


        miFormulario = UserEditForm(request.POST, instance=request.user)


        if miFormulario.is_valid():
            miFormulario.save()


            return render(request, "AppCoder/inicio.html")


    else:


        miFormulario = UserEditForm(instance=request.user)


    return render(request, "AppCoder/editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})   

class cambiarcontrasena(LoginRequiredMixin, PasswordChangeView):
    template_name = 'cambiarcontrasena.html'
    success_url = reverse_lazy('EditarPerfil')

def login_request(request):


    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)


        if form.is_valid():  # Si pasó la validación de Django


            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')


            user = authenticate(username= usuario, password=contrasenia)


            login(request, user)            
            return render(request, "inicio.html", {"mensaje": f'Bienvenido {user.username}'})


           
    else:
        form = AuthenticationForm()


    return render(request, "login.html", {"form": form})


def registro(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"registro.html" ,  {"form":form})
