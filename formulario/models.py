from django.db import models

# Create your models here.

class Empresa(models.Model):
    TIPO_EMPRESA =[
        ('public','Publico'),
        ('private','Privada')
    ]    

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_EMPRESA, default="public")
    categoria =models.CharField(max_length=100)
    direccion= models.TextField()
    telefono = models.CharField(max_length=15)
    correo_contacto= models.EmailField()
    criterios_inclusion = models.TextField()

    def __str__(self) -> str:
        return f"{self.nombre}"

class CriterioInclusion(models.Model):
    criterio = models.CharField(max_length=100, blank=True)
    descripcion_criterio = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.criterio}"
    
    class Meta:
        verbose_name = "Criterio de Inclusion"
        verbose_name_plural = "Criterios de Inclusion"

class Oferta(models.Model):
    MODALIDAD = [
        ('presencial','Presencial'),
        ('remoto','Remoto'),
        ('hibrido','Hibrido')        

    ]
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="publicaciones")
    descripcion_puesto = models.TextField()
    cargo = models.CharField(max_length=100)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    advertencias = models.TextField(blank=True, null=True)  
    modalidad = models.CharField(max_length=50, choices=MODALIDAD, default='presencial')
    fecha_publicacion = models.DateField()
    fecha_cierre = models.DateField()
    criterio_inclusion = models.ManyToManyField(CriterioInclusion, null=True, blank=True)

    def __str__(self):
        return self.cargo

