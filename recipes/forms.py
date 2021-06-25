from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Recipes
from django.utils.translation import gettext_lazy as _

class RecipesCreateForm(forms.ModelForm):
    prep_time_hh = forms.ChoiceField(label=_('Prep Time Hours'),choices=[(x, x) for x in range(0, 24)])
    prep_time_mm = forms.ChoiceField(label=_('Prep Time Minutes'),choices=[(x, x) for x in range(0, 60)])
    cooking_time_hh = forms.ChoiceField(label=_('Cooking Time Hours'),choices=[(x, x) for x in range(0, 24)])
    cooking_time_mm = forms.ChoiceField(label=_('Cooking Time Minutes'),choices=[(x, x) for x in range(0, 60)])
    ingredients = forms.CharField(help_text='Please type each ingredient on a new line',widget=forms.Textarea(attrs={"rows":5, "cols":20}))

    class Meta:
        model = Recipes
        fields = (
            "title",
            "image",
            "category",
            "prep_time_hh",
            "prep_time_mm",
            "cooking_time_hh",
            "cooking_time_mm",
            "ingredients",
            "cooking_steps"
        )
