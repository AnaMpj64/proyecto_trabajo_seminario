from django.shortcuts import render
from .models import Empresa


def listar_empresas(request):
    empresas = Empresa.objects.all()
    contexto = {'empresas':empresas}
    return render(request,'listar_empresas.html',contexto)
