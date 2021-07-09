from django.urls import path, include
from .views import (
    RecipesCreateFormView,
    RecipesListView,
    MyRecipesListView,
    # RecipesDetailView,
    RecipesCreateView,
    RecipesCreateFormView,
    FormSuccessView,
    recipeDetailView,
)

urlpatterns = [
    path("", RecipesListView.as_view(), name="recipes-home"),
    path("<int:pk>/", recipeDetailView, name="recipes-detail"),
    path("new/", RecipesCreateFormView.as_view(), name="recipes-new"),
    path("my-recipes/", MyRecipesListView.as_view(), name="recipes-my"),

]