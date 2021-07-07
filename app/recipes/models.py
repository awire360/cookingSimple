from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.contrib.auth.models import User

# Create your models here.
def get_recipe_image_filepath(self, filename):
    return f'recipe_images/{self.pk}/{"recipe_image.png"}'


def get_default_recipe_image():
    return "recipe_images/default/placeholder.png"


class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class Recipes(models.Model):
    title = models.CharField(max_length=70)
    category = models.ForeignKey(Category, on_delete=PROTECT)
    image = models.ImageField(
        upload_to=get_recipe_image_filepath,
        null=False,
        blank=True,
        default=get_default_recipe_image,
    )
    prep_time_hh = models.SmallIntegerField()
    prep_time_mm = models.SmallIntegerField()
    cooking_time_hh = models.SmallIntegerField()
    cooking_time_mm = models.SmallIntegerField()
    ingredients = models.TextField(blank=False, null=False, max_length=500)
    cooking_steps = models.TextField(verbose_name='Method', max_length=4000, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=PROTECT)

    def get_recipe_image_filepath(self):
        return str(self.image)[str(self.image).index(f"recipe_images/{self.pk}/") :]


