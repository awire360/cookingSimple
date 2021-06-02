from django import forms
from .models import Recipes

class RecipesCreateForm(forms.ModelForm):
    
    class Meta:
        model = Recipes
        fields = ("image", "title","category","cooking_time","body",)