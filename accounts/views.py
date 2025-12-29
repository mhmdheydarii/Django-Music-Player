from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class RegistrationView(TemplateView):
    pass


class LoginView(TemplateView):

    template_name = 'login.html'


class logoutView(TemplateView):
    pass