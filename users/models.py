from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

def get_profile_image_filepath(self, filename):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
    return 'profile_images/default/profile.png'

class Profile(models.Model):
    # This field is required.
    user = models.OneToOneField(User, on_delete=CASCADE)
    
    image = models.ImageField(upload_to=get_profile_image_filepath,null=True, blank=True, default=get_default_profile_image,)

    def get_profile_image_filepath(self):
        return str(self.image)[str(self.image).index(f'profile_images/{self.user.pk}/'):] 

    def __str__(self) -> str:
        return f'{self.user.username}'

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()