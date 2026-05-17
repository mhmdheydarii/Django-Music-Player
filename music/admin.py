from django.contrib import admin
from .models import *
# Register your models here.

class MusicAdmin(admin.ModelAdmin):

    list_display = ['singer', 'title', 'category','created_date', 'published_date', 'status']
    list_filter = ['singer','status', 'category']
    search_fields = ['singer', 'title', 'category']

    filter_horizontal = ['like']

admin.site.register(Music, MusicAdmin)
admin.site.register(Category)

class SingerAdmin(admin.ModelAdmin):
    search_fields = ['name', 'popularity']

admin.site.register(Singer)


class ContactAdmin(admin.ModelAdmin):

    list_display = ['name', 'subject', 'created_date']
    list_filter = ['name', 'created_date']
    search_fields = ['name', 'created_date']

admin.site.register(Contact, ContactAdmin)