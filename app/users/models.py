from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image


# Create your models here.

def get_profile_image_filepath(self, filename):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
    return 'profile_images/default/profile.png'

class Profile(models.Model):
    # This field is required.
    user = models.OneToOneField(User, on_delete=CASCADE)
    
    image = models.ImageField(upload_to=get_profile_image_filepath,null=True, blank=True, default=get_default_profile_image,)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.mode in ("RGBA", "P"): img = img.convert("RGB")
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def SetUserImageDefault(self):
        self.user.profile.image.delete(save=False)  # delete old image file
        self.user.profile.image = get_default_profile_image # set default image
        self.user.profile.save()

    def get_profile_image_filepath(self):
        return str(self.image)[str(self.image).index(f'profile_images/{self.user.pk}/'):] 

    def __str__(self) -> str:
        return f'{self.user.username}'


