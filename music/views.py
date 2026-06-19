from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    FormView,
    RedirectView,
)
from django.views.generic import View
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.utils.decorators import method_decorator
from .models import Music, Singer, Category
from .forms import ContactForm
import time
# Create your views here.

class IndexView(TemplateView):

    template_name = "music/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["singers"] = cache.get_or_set("homepage_singers", lambda:(list(Singer.objects.filter(popularity=True)[:8])), 300)
        context["categories"] = cache.get_or_set("homepage_categories", lambda:(list(Category.objects.all())), 100)
        return context


class ProfileView(DetailView):

    model = User
    template_name = "music/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context["music_like"] = Music.objects.filter(like=user.id)
        return context 



class AlbumsView(ListView):
    model = Singer
    template_name = "music/albums.html"
    paginate_by = 16
    
    def get_queryset(self):
        cache_key = "singers_albume"
        singers = cache.get(cache_key)

        if singers is None:
            singers = list(Singer.objects.all())
            cache.set(cache_key, singers, 300)

        return singers


class SingerDetailView(DetailView):
    model = Singer
    template_name = "music/album_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        singer = self.object

        cache_key = f"singer_music:{singer.id}"
        musics = cache.get(cache_key)
        if musics is None:
            print("before cache")
            musics = list(singer.singer_music.all())
            cache.set(cache_key, musics, 300)

        context["singer_music"] = musics
        return context


class CategoryDetailView(DetailView):

    model = Category
    template_name = "music/album_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.object
        cache_key = f"category_music:{category.id}"
        context["category_music"] = cache.get_or_set(cache_key, lambda:list(category.category_music.all()), 300)
        return context


class LikeMusicView(LoginRequiredMixin, View):

    def post(self, request, pk):
        music = get_object_or_404(Music, pk=pk)
        if music.like.filter(pk=request.user.pk).exists():
            music.like.remove(request.user)
        else:
            music.like.add(request.user)

        source_page = request.GET.get("source")

        if source_page == "singer_detail":
            return redirect("music:singer", slug=music.singer.slug)
        elif source_page == "category_detail":
            return redirect("music:category", slug=music.category.slug)
        elif source_page == "profile":
            return redirect("music:profile", pk=request.user.pk)
        
@method_decorator(cache_page(60 * 5), name='get')
class ContactView(FormView):
    form_class = ContactForm
    template_name = "music/contact.html"
    success_url = reverse_lazy("music:contact")
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        
        try:
            form.save()
            messages.success(self.request, "You`r message has been sent successfully")
        except Exception:
            messages.error(self.request, "Somthing went wrong! Please try again.")
        return super().form_valid(form)

@method_decorator(cache_page(60 * 5), name='get')
class AboutView(TemplateView):
    template_name = "music/about.html"


class SearchView(RedirectView):

    pattern_name = "music/album-detail"

    def get_queryset(self):
        query = self.request.GET.get("s")
        if query:
            return Singer.objects.filter(name__icontains=query)
        return Singer.objects.none()

    def dispatch(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.count() >= 1:
            singer = queryset.first()         
            return redirect('music:singer', slug=singer.slug)
        elif queryset.count() == 0:   
            messages.error(self.request, 'Please Enter a Correct Name!')  
            return redirect('music:index')
        return super().dispatch(request, *args, **kwargs)
