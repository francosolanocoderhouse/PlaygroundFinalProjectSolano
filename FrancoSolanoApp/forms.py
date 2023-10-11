from django import forms

from django.contrib.auth.forms import UserCreationForm,UserModel,UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class VendedorFormulario(forms.Form):
    #Especificar los campos
    documentoVendedor = forms.IntegerField()
    nombreVendedor = forms.CharField(max_length=20)
    apellidoVendedor = forms.CharField(max_length=20)
    
class VentaFormulario(forms.Form):
    #Especificar los campos
    fechaVenta = forms.DateField()
    montoVenta = forms.FloatField()
    documentoVendedor = forms.IntegerField()

class ClienteFormulario(forms.Form):
    #Especificar los campos
    nombreCliente = forms.CharField(max_length=20)
    apellidoCliente = forms.CharField(max_length=20)
    numeroCliente = forms.IntegerField()

class UserEditForm(UserChangeForm):
    
    password = None
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')


    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}