from django import forms
from .models import Empresa

class FormularioEmpresa(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = ['nombre', 'tipo', 'categoria', 'direccion', 'telefono', 'correo_contacto', 'criterios_inclusion', 'logo']
        labels = {
            'nombre' : 'Nombre de la empresa',
            'tipo' : 'Tipo de empresa',
        }
        widgets = {
            'direccion' : forms.Textarea(attrs = 
            {
                'rows' : 2
            })
        }