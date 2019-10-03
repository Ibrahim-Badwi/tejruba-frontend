from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save 
from django.dispatch import receiver


class Settings(models.Model):
    notify_when_reply = models.BooleanField(default=True)
    notify_when_comment = models.BooleanField(default=True)


class CustomUser(AbstractUser):
    settings = models.OneToOneField(Settings, on_delete=models.CASCADE, related_name='user', null=True, blank=True)

    bio = models.TextField(max_length=200, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    job = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.ImageField(upload_to="images/", null=True, blank=True)


@receiver(post_save, sender=CustomUser)
def create_update_settings(sender, instance, created, **kwargs):
    if created:
        Settings.objects.create(user=instance)
    instance.settings.save()