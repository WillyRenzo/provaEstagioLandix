"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from vendedor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list_all_vendors, name='index'),
    path('clientes/<int:pk>/', views.list_vendor_clients, name='list_vendor_clients'),
    path('register_vendor/', views.register_vendor, name='register_vendor'),
    path('register_vendor/submit/', views.set_vendor, name='set_vendor'),
    path('register_client/', views.register_client, name='register_client'),
    path('register_client/submit/', views.set_client, name='set_client'),
    path('edit_vendor/<int:pk>/', views.edit_vendor, name='edit_vendor'),
    path('edit_vendor/<int:pk>/submit/', views.set_edit_vendor, name='set_edit_vendor'),
    path('edit_client/<int:pk>/', views.edit_client, name='edit_client'),
    path('edit_client/<int:pk>/submit/', views.set_edit_client, name='set_edit_client'),
    path('clientes/', views.list_all_clients, name='list_all_clients'),
    path('delete_vendor/<int:pk>/', views.delete_vendor, name='delete_vendor'),
    path('delete_client/<int:pk>/', views.delete_client, name='delete_client'),
]
