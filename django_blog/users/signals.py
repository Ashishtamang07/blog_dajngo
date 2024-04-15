from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

"""signal does something before or after instance is created,
when user is saved(post_save) then send this signals,
signal is recive  to this @reciver and create_profle takes all agruments,
which is send by post_save,
{if user is created then created the instance of profile too} 
"""
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def save_profile(sender, instance,  **kwargs):
    instance.profile.save()