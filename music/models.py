from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Music(models.Model):
    singer = models.ForeignKey('Singer', on_delete=models.CASCADE, related_name='music')
    title = models.CharField(max_length=300)
    audio = models.FileField(upload_to='Music')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL ,null=True, blank=True)
    like = models.ManyToManyField(to=User, blank=True)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField()


    def __str__(self):
        return self.singer.name
    
    class Meta:
        ordering = ['-published_date']



class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True)
    image = models.ImageField(upload_to='Category/', default="Category/کلاسیک.jpg",  null=True, blank=True)

    def __str__(self):
        return self.name
    


class Singer(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True)
    image = models.ImageField(upload_to='Singer')
    year_started = models.IntegerField(default=2026)
    popularity = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("music:singer", kwargs={"slug":self.slug})
    


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=350)
    subject = models.CharField(max_length=400)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name