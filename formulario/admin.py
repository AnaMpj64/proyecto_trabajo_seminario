from django.contrib import admin
from .models import Empresa,CriterioInclusion,Oferta

# Register your models here.

admin.site.register(Empresa)
admin.site.register(CriterioInclusion)
admin.site.register(Oferta)
