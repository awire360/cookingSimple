from django.db import models
from django.db.models.deletion import PROTECT
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Recipes(models.Model):
    image = models.ImageField(upload_to="media/")
    title = models.CharField(max_length=70)
    category = models.ForeignKey(Category, on_delete=PROTECT)
    cooking_time = models.TimeField(auto_now=False, auto_now_add=False)
    body = models.TextField()
    plain_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=PROTECT)
