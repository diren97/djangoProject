from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic  import CreateView,FormView
from django.contrib.auth.forms import UserCreationForm

class SignInView(LoginView):
    template_name= 'profiles/signin.html'

class RegisterUserView(FormView,SuccessMessageMixin):
    form_class = UserCreationForm
    template_name = 'profiles/register.html'
    success_url = reverse_lazy('anasayfa')
    success_message ='Basari ile kayit oldunuz'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)