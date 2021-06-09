from django import forms
from django.utils.regex_helper import Choice
from .models import Recipes

class RecipesCreateForm(forms.ModelForm):

    method = forms.CharField(max_length=250)
    prep_time_hh = forms.ChoiceField(choices=[(x, x) for x in range(1, 24)])
    prep_time_mm = forms.ChoiceField(choices=[(x, x) for x in range(1, 60)])
    cooking_time_hh = forms.ChoiceField(choices=[(x, x) for x in range(1, 24)])
    cooking_time_mm = forms.ChoiceField(choices=[(x, x) for x in range(1, 60)])

    class Meta:
        model = Recipes
        fields = (
            "image",
            "recipe_title",
            "category",
            "prep_time_hh",
            "prep_time_mm",
            "cooking_time_hh",
            "cooking_time_mm",
            "ingredients",
            "method"
        )
