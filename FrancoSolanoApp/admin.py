from django.contrib import admin
from .models import * 

# Register your models here.
#registramos los modelos

admin.site.register(vendedor)
admin.site.register(venta)
admin.site.register(cliente)
admin.site.register(avatar)

