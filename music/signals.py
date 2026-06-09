from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache

from .models import Category, Singer

# Clear singer cache on update
@receiver([post_save, post_delete], sender=Singer)
def clear_singer_cache(sender, instance, **kwargs):
    cache.delete("homepage_singers")

# Clear category cache on update
@receiver([post_save, post_delete], sender=Category)
def clear_category_cache(sender, instance, **kwargs):
    cache.delete("homepage_categories")
