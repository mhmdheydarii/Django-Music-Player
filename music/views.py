from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class IndexView(TemplateView):

    template_name = 'index.html'



class SingersView(TemplateView):

    template_name = 'singers.html'


class BlogView(TemplateView):

    template_name = 'blog.html'


class ContactView(TemplateView):

    template_name = 'contact.html'