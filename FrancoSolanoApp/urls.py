from django.urls import path
from FrancoSolanoApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), 
    path('vendedores', views.vendedores, name="Vendedores"),
    path('vendedores_formulario', views.vendedores_formulario, name="vendedores_formulario"),
    path('ventas_formulario', views.venta_formulario, name="ventas_formulario"),
    path('clientes', views.cliente_formulario, name="clientes_formulario"),
    path('buscar_ventas', views.buscar_ventas, name="buscar_ventas"),
    path('buscar', views.buscar,name="buscar"),
    path('about', views.about,name="about"),
    path('editarperfil', views.editarPerfil,name="editarperfil"),
    path('cambiarcontrasena', views.cambiarcontrasena.as_view,name="cambiarcontrasena"),
    path('pages', views.pages,name="pages"),
    path('login', views.login_request,name="login"),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('registro', views.registro,name="registro")
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
