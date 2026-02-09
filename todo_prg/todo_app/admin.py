from django.contrib import admin
from .models import Todo # Importamos el modelo que acabamos de crear

# Register your models here.
admin.site.register(Todo)