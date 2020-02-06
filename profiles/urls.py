from django.urls import path, include
from profiles.views import *
from django.contrib.auth.views import LogoutView,LoginView

app_name = 'profiles'

urlpatterns = [
    path('signin/',SignInView.as_view(), name ='signin'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('giris/',LoginView.as_view(template_name='profiles/signin.html'),name='giris'),
]