from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, ProfileForm, CustomUserChangeForm
from .models import Profile
from django.contrib.auth.views import LoginView
from django.views import View
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
# Create your views here.


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

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



# class UserProfile(LoginRequiredMixin, View):
#     template_name = 'accounts/profile.html'
#     def get(self, request, *args, **kwargs):
#         user_form = CustomUserChangeForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.user_profile)
#         context = {
#             'user_form':user_form,
#             'profile_form':profile_form,
#         }
#         return render(request, self.template_name, context)
#     def post(self, request, *args, **kwargs):
#         user_form = CustomUserChangeForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, request.FILES,instance=request.user.user_profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Update Info Successfull')
#             return redirect('accounts:profile')
#         context = {
#             'user_form':user_form,
#             'profile_form':profile_form,   
#         }
#         return render(request, self.template_name, context)

def profile(request):
    obj = Profile.objects.get(user=request.user)
    user_form = CustomUserChangeForm(request.POST or None, instance=request.user)
    profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user.user_profile)
    if is_ajax(request):
        if profile_form.is_valid() and user_form.is_valid():
            instance1 = user_form.save()
            instance2 = profile_form.save()
            print(instance1.first_name)
            print(instance1.last_name)
            return JsonResponse({
                'bio': instance2.bio,
                'avatar': instance2.avatar.url,
                'username': instance1.username,
                'email': instance1.email,
                'first_name': instance1.first_name,
                'last_name': instance1.last_name,
                'created': instance2.created,
                'updated':instance2.updated,
            })
    context = {
        'obj':obj,
        'user_form':user_form,
        'profile_form':profile_form, 
    }
    return render(request, "accounts/profile.html", context)