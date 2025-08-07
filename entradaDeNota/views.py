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

        nombreAutor = request.POST.getlist('nombreAutor[]')
        correoAutor = request.POST.getlist('correoAutor[]')
        telefonoAutor = request.POST.getlist('telefonoAutor[]')

        if not nombreAutor and not correoAutor and not telefonoAutor:
            return HttpResponse("Los campos del autor son obligatorios.")

        nombreAsesor = request.POST.getlist('nombreAsesor[]')
        correoAsesor = request.POST.getlist('correoAsesor[]')
        telefonoAsesor = request.POST.getlist('telefonoAsesor[]')
        # Guardar los datos en la base de datos
    
        

        for nombre, correo, telefono in zip(nombreAutor, correoAutor, telefonoAutor):
            Autor.objects.create(
                nombreAutor=nombre,
                correoAutor=correo,
                telefonoAutor=telefono,
                proyecto=proyecto
            )
        
        for nombre, correo, telefono in zip(nombreAsesor, correoAsesor, telefonoAsesor):
            Asesor.objects.create(
                nombreAsesor=nombre,
                correoAsesor=correo,
                telefonoAsesor=telefono,
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
