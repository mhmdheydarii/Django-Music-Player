from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache

from .models import Category, Singer, Music, Category


# Clear singer cache on update
@receiver([post_save, post_delete], sender=Singer)
def clear_singer_cache(sender, **kwargs):
    cache.delete("homepage_singers")


# Clear category cache on update
@receiver([post_save, post_delete], sender=Category)
def clear_category_homepage_cache(sender, **kwargs):
    cache.delete("homepage_categories")


@receiver([post_save, post_delete], sender=Singer)
def clear_singer_albume_cache(sender, **kwargs):
    cache.delete("Singers_albume")


# Clear singer music cache on update
@receiver([post_save, post_delete], sender=Music)
def clear_music_cache(sender, instance, **kwargs):
    cache.delete(f"singer_music:{instance.singer_id}")


@receiver([post_save, post_delete], sender=Category)
def clear_category_cache(sender, instance, **kwargs):
    cache.delete(f"category_music:{instance.category_id}")
