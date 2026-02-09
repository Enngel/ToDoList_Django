"""
URL configuration for todo_prg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# FIX 1: Import 'include' from django.urls, not as a separate module
from django.urls import path, include

# FIX 2: Use square brackets [] for the list, not curly braces {}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_app.urls')),
]