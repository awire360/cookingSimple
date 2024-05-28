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

class Recipe(models.Model):
    category = models.ForeignKey(Category, on_delete=PROTECT)
    image = models.ImageField(
        upload_to=get_recipe_image_filepath,
        null=False,
        blank=True,
        default=get_default_recipe_image,
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    cooking_time = models.IntegerField(help_text="Time in minutes")
    servings = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=PROTECT)
    public = models.BooleanField(default=False)
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)

    def __str__(self):
        return self.title
    
    def get_recipe_image_filepath(self):
        return str(self.image)[str(self.image).index(f"recipe_images/{self.pk}/") :]

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    unit = models.CharField(max_length=50)

    class Meta:
        unique_together = ('recipe', 'ingredient')

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.ingredient.name} for {self.recipe.title}"


class Step(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='steps', on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    description = models.TextField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Step {self.order} for {self.recipe.title}"

