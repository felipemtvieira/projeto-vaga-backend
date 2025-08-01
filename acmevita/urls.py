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

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from departamentos.views import DepartamentoViewSet
from colaboradores.views import ColaboradorViewSet
from dependentes.views import DependenteViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="API de Colaboradores",
      default_version='v1',
      description="Documentação da API para o gerenciamento de colaboradores, departamentos e dependentes.",
      contact=openapi.Contact(email="felipemtvieira@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('departamentos', DepartamentoViewSet, basename='departamento')
router.register('colaboradores', ColaboradorViewSet, basename='colaborador')
router.register('dependentes', DependenteViewSet, basename='dependente')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
