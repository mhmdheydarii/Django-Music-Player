from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache

from .models import Category, Singer

# Clear singer cache on update
@receiver(post_save, sender=Singer)
def clear_singer_cache_on_save(sender, instance, **kwargs):
    cache.delete("homepage_singers")

@receiver(post_delete, sender=Singer)
def clear_singer_cache_on_delete(sender, instance, **kwargs):
    cache.delete("homepage_singers")

# Clear category cache on update
@receiver(post_save, sender=Category)
def clear_category_cache_on_save(sender, instance, **kwargs):
    cache.delete("homepage_categories")

@receiver(post_delete, sender=Category)
def clear_category_cache_on_delete(sender, instance, **kwargs):
    cache.delete("homepage_categories")