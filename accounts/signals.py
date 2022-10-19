from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, *args, **kwargs):
    if created:
        print(sender)
        print(instance)
        print(created)
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def post_save(sender, instance, *args, **kwargs):
    instance.user_profile.save()