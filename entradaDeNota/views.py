from django.shortcuts import render, HttpResponse, redirect
from entradaDeNota.models import Proyecto, Autor, Asesor

# Create your views here.



def formulario(request): 
    return render(request, 'formulario.html')

def guardar_formulario(request): 

    if request.method == 'POST':

        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']

        # Validar que los campos no estén vacíos
        if not titulo:
            return HttpResponse("El campos título es obligatorio.")
        

        proyecto = Proyecto(    
                titulo = titulo,
                descripcion = descripcion
                )
        proyecto.save()

        nombreAutor1 = request.POST.getlist('nombreAutor[]')
        correoAutor1 = request.POST.getlist('correoAutor[]')
        telefonoAutor1 = request.POST.getlist('telefonoAutor[]')

        if not nombreAutor1 and not correoAutor1 and not telefonoAutor1:
            return HttpResponse("Los campos del autor son obligatorios.")

        nombreAsesor1 = request.POST.getlist('nombreAsesor[]')
        correoAsesor1 = request.POST.getlist('correoAsesor[]')
        telefonoAsesor1 = request.POST.getlist('telefonoAsesor[]')
        # Guardar los datos en la base de datos
    
        

        for nombre, correo, telefono in zip(nombreAutor1, correoAutor1, telefonoAutor1):
            Autor.objects.create(
                nombreAutor1=nombre,
                correoAutor1=correo,
                telefonoAutor1=telefono,
                proyecto=proyecto
            )
        
        for nombre, correo, telefono in zip(nombreAsesor1, correoAsesor1, telefonoAsesor1):
            Asesor.objects.create(
                nombreAsesor1=nombre,
                correoAsesor1=correo,
                telefonoAsesor1=telefono,
                proyecto=proyecto
            )

        return HttpResponse("Datos guardados correctamente")

"""
        autor = Autor(
                nombreAutor1 = nombreAutor1,
                correoAutor1 = correoAutor1,
                telefonoAutor1 = telefonoAutor1,
                proyecto = proyecto
                
        )
        autor.save()

        asesor = Asesor(
                nombreAsesor1 = nombreAsesor1,
                correoAsesor1 = correoAsesor1,
                telefonoAsesor1= telefonoAsesor1,
                proyecto = proyecto
        )
        asesor.save()
"""





"""
def iniciar_sesion(request, redirigir=0):
    if redirigir==1:
            return redirect("contacto", nombre="Jesus", apellido="Carreiro")
    return render(request, 'iniciarSesion.html')




def contacto(request, nombre="", apellido=""):

    html = ""
    if nombre and apellido:
        html += "<p>El nombre completo del contacto es:</p> "
        html += f"<h3>{nombre} {apellido}<h3/>"
    return HttpResponse (layout+f"<h2>Contacto</h2>"+html)
"""
