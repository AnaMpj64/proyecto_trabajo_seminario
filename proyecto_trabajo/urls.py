"""
URL configuration for proyecto_trabajo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from formulario.views import listar_empresas, detalle_empresa, crear_empresa, perfil
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('empresas/',listar_empresas,name='listar_empresas'),
    path('empresa/<int:empresa_id>/', detalle_empresa, name='detalle_empresa'),
    path('empresa/nueva/',crear_empresa,name='crear_empresa'),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', perfil),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
