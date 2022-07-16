from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.views.generic import View,TemplateView,ListView, UpdateView, CreateView, DeleteView
from .forms import FormularioLogin


def Inicio(request):
   
    return render(request,'principales\index.html')
    

class Login(FormView):
    template_name = 'principales\login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('inicio:index-principal')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def logoutUsuario(request):
    logout(request)
    return redirect('inicio:index-principal')
