from django.contrib import admin
from .models import Music, Singer, Contact
# Register your models here.

class MusicAdmin(admin.ModelAdmin):

    list_display = ['singer', 'title', 'created_date', 'published_date', 'status']
    list_filter = ['singer','status']
    search_fields = ['singer', 'title']

admin.site.register(Music, MusicAdmin)
admin.site.register(Singer)


class ContactAdmin(admin.ModelAdmin):

    list_display = ['name', 'subject', 'created_date']
    list_filter = ['name', 'created_date']
    search_fields = ['name', 'created_date']

admin.site.register(Contact, ContactAdmin)