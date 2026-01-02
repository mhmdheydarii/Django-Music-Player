from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, FormView
from .models import Music, Singer
from django.shortcuts import get_object_or_404
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.


class IndexView(FormView):

    form_class = ContactForm
    template_name = 'index.html'
    success_url = reverse_lazy('music:index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['musics'] = Music.objects.filter(status=True)[:6]
        context['singers'] = Singer.objects.all()[:7]
        return context
    
    def form_valid(self, form):
        try:
            form.save()
            messages.success(self.request, 'Your message has been sent successfully')
        except Exception:
            messages.error(self.request, 'Somthing went wrong. Please try again')
        return super().form_valid(form)
        

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



