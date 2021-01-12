from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import Profile, Wine_Classification


@receiver(post_save, sender=User)
def user_created_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('Profile created!')


@receiver(post_save, sender=User)
def user_updated_profile(sender, instance, created, **kwargs):
    instance.profile.save()
    print('Profile updated!')
