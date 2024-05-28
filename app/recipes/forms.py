from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Recipe
from django.utils.translation import gettext_lazy as _

class RecipeCreateForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = (
            "title",
            "image",
            "category",
            "description",
            "cooking_time",
            "servings",
        )
