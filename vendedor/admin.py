from django.contrib import admin
from .models import Vendedor, Cliente

# ADICIONAR AO 127.0.0.1:8000/admin

admin.site.register(Vendedor)
admin.site.register(Cliente)
