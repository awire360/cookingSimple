from django.contrib import admin
from .models import Recipe, Category

# Register your models here.

class RecipesAdmin(admin.ModelAdmin):
    list_display = ['title','category', 'author']

admin.site.register(Recipe, RecipesAdmin)
admin.site.register(Category)