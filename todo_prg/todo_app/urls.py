from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),

    # NUEVAS RUTAS:
    # <str:name> significa que la URL espera un texto (el nombre de la tarea)
    # Ejemplo: /delete/Comprar pan/
    path('delete/<str:name>/', views.deleteTask, name='delete'),
    path('update/<str:name>/', views.updateTask, name='update'),
]