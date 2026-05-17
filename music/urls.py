from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('profile/<int:pk>/?source=profile/', views.ProfileView.as_view(), name='profile'),
    path('albums/', views.AlbumsView.as_view(), name='albums'),
    path('singer/<slug:slug>/?source=singer_detail/', views.SingerDetailView.as_view(), name='singer'),
    path('category/<slug:slug>/?source=category_detail/', views.CategoryDetailView.as_view(), name='category'),
    path('music/<int:pk>/like/', views.LikeMusicView.as_view(), name='like-music'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('search/', views.SearchView.as_view(), name='search'),
]