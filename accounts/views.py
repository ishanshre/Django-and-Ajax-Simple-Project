from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.views import LoginView
from django.views import View
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
class RegisterView(View):
    template_name = 'accounts/register.html'
    def get(self, request, *args, **kwargs):
        register_form = RegisterForm()
        context = {
            'register_form':register_form,
        }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'User Created Successfully')
            return redirect('crud_ajax:index')
        context = {
            'register_form':register_form,
        }
        return render(request, self.template_name, context)


class UserLoginView(SuccessMessageMixin,LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_message = 'login successfull'
    
    
    