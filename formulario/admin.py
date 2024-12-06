from django.contrib import admin
from .models import Empresa,CriterioInclusion,Oferta, Perfil

# Register your models here.

admin.site.register(Empresa)
admin.site.register(CriterioInclusion)
admin.site.register(Oferta)

@admin.register(Perfil)
class Perfiladmin(admin.ModelAdmin):
    list_display = (
        'user', 
        'cedula',
        )
