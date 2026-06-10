from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache

from .models import Category, Singer, Music

# Clear singer cache on update
@receiver([post_save, post_delete], sender=Singer)
def clear_singer_cache(sender, **kwargs):
    cache.delete("homepage_singers")

# Clear category cache on update
@receiver([post_save, post_delete], sender=Category)
def clear_category_cache(sender, **kwargs):
    cache.delete("homepage_categories")

# Cleare like music cache on update
@receiver([post_save, post_delete], sender=Music)
def cleare_like_music(sender, instance, **kwargs):
    cache.delete(f"music_like_{instance.user.id}")