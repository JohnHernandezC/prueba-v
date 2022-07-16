from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ObjectDoesNotExist
from usuariosApp.models import *
from usuariosApp.forms import *



def crearEmpleados(request):
    if request.method == 'POST':
        EmpleadosForm=FormularioUsuario(request.POST)#recibe datos almacenados en la peticion POST
        if EmpleadosForm.is_valid(): # valida el formulario
            EmpleadosForm.save()
            return redirect('crud:listar-Empleados')
        
    else: 
        EmpleadosForm=FormularioUsuario()
        
    return render(request,'empleados\index.html',{'EmpleadosForm':FormularioUsuario})

def editarEmpleadosr (request,id):
    EmpleadosForm=None
    error=None
    try:
        EmpleadosE=Empleados.objects.get(id=id)
        if request.method=='GET':
            EmpleadosForm=FormularioUsuario(instance=EmpleadosE)
        else:
            EmpleadosForm=FormularioUsuario(request.POST, instance=EmpleadosE)
            if EmpleadosForm.is_valid(): # valida el formulario
                EmpleadosForm.save()
                return redirect('crud:listar-Empleados')
    except ObjectDoesNotExist as e:
        error=e
        
    return render(request,'empleados\index.html',{'EmpleadosForm':EmpleadosForm,'error':error})

    
def listarEmpleados (request):
     EmpleadosL=Empleados.objects.all()
     return render(request,'empleados\listarE.html',{'EmpleadosL':EmpleadosL})


def eliminarEmpleados (request,id):
    Empleado=Empleados.objects.get(id=id)
    if request.method=='POST':
        Empleado.delete()
        return redirect('crud:listar-Empleados')
    return render(request,'empleados\eliminar.html',{'Empleados':Empleado})


#-//////////////////////////////////////////////////////////


def crearExperiencia(request):
    courrent_user=get_object_or_404(Empleados,pk=request.user.pk)
    
    if request.method == 'POST':
        forms1=ExperienciaForms(request.POST)
        if forms1.is_valid():
                post=forms1.save(commit=False)
                post.empleado_id_Ex=courrent_user
                post.save()
                return redirect('crud:listar-Experiencia')    
                        
            


        
    else: 
        ExperienciaForm=ExperienciaForms()
        
    return render(request,'experiencia\index.html',{'ExperienciaForm':ExperienciaForms})


    

def editarExperiencia (request,id):
    ExperienciaForm=None
    error=None
    try:
        ExperienciaE=Experiencia.objects.get(id=id)
        if request.method=='GET':
            ExperienciaForm=ExperienciaForms(instance=ExperienciaE)
        else:
            ExperienciaForm=ExperienciaForms(request.POST, instance=ExperienciaE)
            if ExperienciaForm.is_valid(): # valida el formulario
                ExperienciaForm.save()
                return redirect('crud:listar-Experiencia')
    except ObjectDoesNotExist as e:
        error=e
        
    return render(request,'experiencia\index.html',{'ExperienciaForm':ExperienciaForm,'error':error})

    
def listarExperiencia (request):
     ExperienciaL=Experiencia.objects.all()
     return render(request,'experiencia\listarE.html',{'ExperienciaL':ExperienciaL})


def eliminarExperiencia (request,id):
    Experiencia1=Experiencia.objects.get(id=id)
    if request.method=='POST':
        Experiencia1.delete()
        return redirect('crud:listar-Experiencia')
    return render(request,'experiencia\eliminar.html',{'Experiencia':Experiencia})



#-//////////////////////////////////////////////////////////


def crearEstudios(request):
    courrent_user=get_object_or_404(Empleados,pk=request.user.pk)
    
    if request.method == 'POST':
        forms1=EstudiosForms(request.POST)
        if forms1.is_valid():
                post=forms1.save(commit=False)
                post.empleado_id_Em=courrent_user
                post.save()
                return redirect('crud:listar-Estudios')       
    else: 
        EstudiosForm=EstudiosForms()
        
    return render(request,'estudios\index.html',{'ExperienciaForm':EstudiosForm})
def editarEstudios (request,id):
    ExperienciaForm=None
    error=None
    try:
        ExperienciaE=Estudios.objects.get(id=id)
        if request.method=='GET':
            ExperienciaForm=EstudiosForms(instance=ExperienciaE)
        else:
            ExperienciaForm=EstudiosForms(request.POST, instance=ExperienciaE)
            if ExperienciaForm.is_valid(): # valida el formulario
                ExperienciaForm.save()
                return redirect('crud:listar-Estudios')
    except ObjectDoesNotExist as e:
        error=e
    return render(request,'estudios\index.html',{'ExperienciaForm':ExperienciaForm,'error':error})

    
def listarEstudios (request):
     ExperienciaL=Estudios.objects.all()
     return render(request,'estudios\listarE.html',{'EstudiosL':ExperienciaL})


def eliminarEstudios (request,id):
    Estudios1=Estudios.objects.get(id=id)
    if request.method=='POST':
        Estudios1.delete()
        return redirect('crud:listar-Estudios')
    return render(request,'estudios\eliminar.html',{'Experiencia':Estudios1})




