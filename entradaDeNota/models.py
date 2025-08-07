from django.db import models

# Create your models here.

class Proyecto(models.Model):
    titulo= models.CharField(max_length=100)
    descripcion= models.TextField()
    fechaRegistro= models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.titulo  # Aquí defines qué se mostrará como nombre legible

class Autor(models.Model):
    nombreAutor= models.CharField(max_length=100)
    correoAutor= models.EmailField()
    telefonoAutor= models.CharField(max_length=20)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='autores')  

    def __str__(self):
        return self.nombreAutor  # Aquí defines qué se mostrará como nombre legible

class Asesor(models.Model):
    nombreAsesor= models.CharField(max_length=100)
    correoAsesor= models.EmailField()
    telefonoAsesor= models.CharField(max_length=20)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='asesores')

    def __str__(self):
        return self.nombreAsesor  # Aquí defines qué se mostrará como nombre legible




