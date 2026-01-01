from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Music, Singer
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.


class IndexView(TemplateView):

    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['musics'] = Music.objects.filter(status=True)[:6]
        context['singers'] = Singer.objects.all()[:7]
        return context

class SingerMusicsView(ListView):
    model = Singer
    context_object_name = 'musics'
    paginate_by = 2

    def get_queryset(self):
        singer_id = self.kwargs['pk']
        return Music.objects.filter(singer__id = singer_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['singer'] = Singer.objects.get(id=self.kwargs['pk'])
        return context

class SingersView(TemplateView):

    template_name = 'singers.html'


class BlogView(TemplateView):

    template_name = 'blog.html'


class ContactView(TemplateView):

    template_name = 'contact.html'

