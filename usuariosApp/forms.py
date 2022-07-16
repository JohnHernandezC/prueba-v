from django import forms
from django.forms import ModelForm 
from django.contrib.auth.forms import AuthenticationForm
from .models import *


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


class FormularioUsuario(forms.ModelForm):
    
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput(
        attrs={
            'clase':'form-control',
            'placeholder':'Ingrese su contraseña...',
            'id':'password1',
            'required':'required',
        }
        
    ))
    
    password2 = forms.CharField(label="contraseña de confirmacion", widget=forms.PasswordInput(
        attrs={
            'clase':'form-control',
            'placeholder':'Ingrese nuevamente su contraseña...',
            'id':'password2',
            'required':'required',
        }
        
    ))
    class Meta:
        model=Empleados
        fields=('u_identificacion','u_apellidos','u_nombres','u_tipoDpocumento','u_tipoSangre','u_telefono','u_email','u_imagen')
        widgets = {
             'u_identificacion': forms.TextInput(
              attrs={
                    'clase':'form-control',
                     'placeholder':'Ingrese su numero de documento',
                     'required':'required',
            
                }  
            ), 'u_apellidos': forms.TextInput(
              attrs={
                    'clase':'form-control',
                     'placeholder':'Ingrese sus apellidos',
                     'required':'required',
            
                }  
            ),'u_nombres': forms.TextInput(
              attrs={
                    'clase':'form-control',
                     'placeholder':'Ingrese su nombre',
                     'required':'required',
            
                }  
            ),
            'u_telefono': forms.TextInput(
              attrs={
                    'clase':'form-control',
                     'placeholder':'Ingrese su telefono',
                     'required':'required',
            
                }  
            ),
            'u_email': forms.EmailInput(
                attrs={
                    'clase':'form-control',
                     'placeholder':'Ingrese su correo',
            
                }
            ),'u_imagen ':forms.ClearableFileInput(),
            
            
            
        }
        
    def clean_password2(self):
        #validacion de contraseña (valida que ambas contraseñas sean iguales)
        password1=self.cleaned_data.get('password1')#cleaned_data es donde estan almacenados los datos que se lamacenaron desde el formulario y se obtienen con el get y la key
        password2=self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('contraseñas no coinciden')
        return password2
    
    def save(self,commit=True):
        print(self.cleaned_data)
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])#set encripta directamente la contraseña
        if commit:
            user.save()
        return user
    
class PersonaForm(ModelForm):
    class Meta:
        model=Empleados
        fields=['is_userp']
        
        

       
        
class  ExperienciaForms (ModelForm):
    class Meta:
        model=Experiencia
        exclude=('empleado_id_Ex',)
        
        widgets = {
             'fechas': forms.DateInput(
              attrs={
                    'clase':'form-control',
                     'required':'required',
            
                }  
            ),
        }
class EstudiosForms (ModelForm):
    class Meta:
        model=Estudios
        exclude=('empleado_id_Em',)
        
        widgets = {
             'fechas': forms.DateInput(
              attrs={
                    'clase':'form-control',
                     'required':'required',
            
                }  
            ),
        }