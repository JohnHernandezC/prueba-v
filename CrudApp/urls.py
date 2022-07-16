from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('crearU/',crearEmpleados,name='crear-Empleados'),
    path('actualizarU/<int:id>/',login_required(editarEmpleadosr),name='actualizar-Empleados'),
    path('',login_required(listarEmpleados),name='listar-Empleados'),
    path('borrarU/<int:id>/',login_required(eliminarEmpleados),name='borrar-Empleados'),
    
    path('listarE/',login_required(listarExperiencia),name='listar-Experiencia'),
    path('crearE/',login_required(crearExperiencia),name='crear-Experiencia'),
    path('actualizarE/<int:id>/',login_required(editarExperiencia),name='actualizar-Experiencia'),
    path('borrarE/<int:id>/',login_required(eliminarExperiencia) ,name='borrar-Experiencia'),
    
    path('listarEs/',login_required(listarEstudios),name='listar-Estudios'),
    path('crearEs/',login_required(crearEstudios),name='crear-Estudios'),
    path('actualizarEs/<int:id>/',login_required(editarEstudios),name='actualizar-Estudios'),
    path('borrarEs/<int:id>/',login_required(eliminarEstudios) ,name='borrar-Estudios'),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)