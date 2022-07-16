from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager ,PermissionsMixin    

class UsuarioManager(BaseUserManager):
    def _create_user(self, u_email, u_nombres, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            u_email=u_email,
            u_nombres=u_nombres,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self,u_email,  u_nombres, is_staff, password=None, **extra_fields):
        return self._create_user(u_email,  u_nombres, password, is_staff, False, **extra_fields)
    
    def create_superuser(self,u_email,  u_nombres,password = None,**extra_fields):
        return self._create_user(u_email,  u_nombres, password, True, True, **extra_fields) 
    


class tipoDocumento(models.Model):
    nombre=models.CharField(max_length=50)
    class Meta:
        verbose_name = 'tipoDocumento'
        verbose_name_plural ='tipoDocumentos'
        
    def __str__(self):
        return self.nombre

class tipoSangre(models.Model):
    nombre=models.CharField(max_length=50)
    class Meta:
        verbose_name = 'tipoSangre'
        verbose_name_plural ='tiposSangre'
        
    def __str__(self):
        return self.nombre


class Empleados(AbstractBaseUser,PermissionsMixin ):
    
    u_nombres = models.CharField(max_length=50) 
    u_apellidos = models.CharField(max_length=50)
    u_tipoDpocumento = models.ForeignKey(tipoDocumento, on_delete=models.CASCADE,null=True )
    u_identificacion = models.CharField(max_length=15)
    u_telefono= models.CharField(max_length=50)
    u_email = models.CharField(max_length=50,unique=True)
    u_tipoSangre= models.ForeignKey(tipoSangre, on_delete=models.CASCADE, null=True)
    u_imagen = models.ImageField('Imagen de Empleado', max_length=200,blank = True,null = True)
    is_active = models.BooleanField(default = True)
    is_staff  = models.BooleanField(default = False)
    is_userp = models.BooleanField(default = False)
    objects = UsuarioManager()
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural ='Empleados'
        ordering = ['u_apellidos']
    def __str__(self):
        return self.u_apellidos
    USERNAME_FIELD='u_email' 
    REQUIRED_FIELDS=['u_nombres','u_identificacion']
    
    

class Estudios (models.Model):
    empleado_id_Em = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    fechas=models.DateField()
    estudios=models.CharField(max_length=50)
    institucion= models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Estudio'
        verbose_name_plural ='Estudios'
        
    def __str__(self):
        return self.estudios
    
class Experiencia (models.Model):
    empleado_id_Ex = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    fechas=models.DateField()
    empresa=models.CharField(max_length=50)
    jefe= models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    responsabilidades = models.TextField()
    logros = models.TextField()
    
    class Meta:
        verbose_name = 'Experiencia'
        verbose_name_plural ='Experiencias'
        
    def __str__(self):
        return self.cargo
    
    
    
    