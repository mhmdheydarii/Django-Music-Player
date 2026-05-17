
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Singer

class SingerSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        return Singer.objects.all()
    

