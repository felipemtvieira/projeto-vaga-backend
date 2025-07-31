"""
URL configuration for acmevita project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from departamentos.views import DepartamentoViewSet
from colaboradores.views import ColaboradorViewSet
from dependentes.views import DependenteViewSet

router = routers.DefaultRouter()
router.register('departamentos', DepartamentoViewSet, basename='departamento')
router.register('colaboradores', ColaboradorViewSet, basename='colaborador')
router.register('dependentes', DependenteViewSet, basename='dependente')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
