from django.contrib import admin
from .models import Recipes, Category

# Register your models here.

class RecipesAdmin(admin.ModelAdmin):
    list_display = ['title','category', 'author']

admin.site.register(Recipes, RecipesAdmin)
admin.site.register(Category)