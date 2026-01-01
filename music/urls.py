from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('singer/<int:pk>/', views.SingerMusicsView.as_view(), name='singer'),
    path('singers/', views.SingersView.as_view(), name='singers'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]