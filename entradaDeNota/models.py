from django.db import models

# Create your models here.

class Proyecto(models.Model):
    titulo= models.CharField(max_length=100)
    descripcion= models.TextField()
    fechaRegistro= models.DateTimeField(auto_now_add=True) 


class Autor(models.Model):
    nombreAutor1= models.CharField(max_length=100)
    correoAutor1= models.EmailField()
    telefonoAutor1= models.CharField(max_length=20)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='autores')  

class Asesor(models.Model):
    nombreAsesor1= models.CharField(max_length=100)
    correoAsesor1= models.EmailField()
    telefonoAsesor1= models.CharField(max_length=20)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='asesores')




