from django.shortcuts import redirect, render, get_object_or_404

from formulario.forms import FormularioEmpresa
from .models import Empresa, Oferta


def listar_empresas(request):
    empresas = Empresa.objects.all()
    contexto = {'empresas':empresas}
    if request.user.is_superuser:
        print (f'Hola Superusuario {request.user}')

    return render(request,'listar_empresas.html',contexto)

def detalle_empresa(request, empresa_id):
    print ('metodo', request.method)
    empresa = get_object_or_404(Empresa, id=empresa_id)
    ofertas = Oferta.objects.filter(empresa=empresa)
    contexto = {
        'empresa': empresa, 
        'ofertas': ofertas,
        }
    return render(request, 'detalle_empresa.html', contexto)

def crear_empresa(request):
    if request.method == 'POST':
        formulario = FormularioEmpresa(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_empresas')
    formulario = FormularioEmpresa()
    contexto = {
        'formulario' : formulario
    }
    return render(request, 'crear_empresa.html', contexto)

