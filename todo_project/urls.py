from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.site_header),
    path('admin/', admin.site.urls),
    path('', include('todo_app.urls')),
    path('app/', TemplateView.as_view(template_name='index.html'), name='index'),
]
