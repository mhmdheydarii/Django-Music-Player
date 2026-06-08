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

        singers = cache.get("homepage_singers")
        
        if singers is None:
            singers = list(Singer.objects.filter(popularity=True)[:8])
            cache.set("homepage_singers", singers, 300)

        context["singers"] = singers
        context["categories"] = cache.get_or_set("homepage_categories", lambda:(list(Category.objects.all())), 300)
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
    context_object_name = "singers"


class SingerDetailView(DetailView):
    model = Singer
    template_name = "music/album_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        singer = self.get_object()
        context["singer_music"] = Music.objects.filter(singer=singer)
        return context


class CategoryDetailView(DetailView):

    model = Category
    template_name = "music/album_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context["category_music"] = Music.objects.filter(category=category)
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
