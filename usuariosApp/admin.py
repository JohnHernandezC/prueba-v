from django.contrib import admin
from .models import *

# Register your models here.

class empleados_admin(admin.ModelAdmin):
    list_display=("u_identificacion","u_nombres")
    
class empleados_admin(admin.ModelAdmin):
    list_display=("u_identificacion","u_nombres")
    
class empleados_admin(admin.ModelAdmin):
    list_display=("u_identificacion","u_nombres")

admin.site.register(Empleados,empleados_admin)
admin.site.register(Experiencia)
admin.site.register(Estudios)
admin.site.register(tipoSangre)
admin.site.register(tipoDocumento)
