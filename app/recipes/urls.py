from django.urls import path, include
from recipes import views

urlpatterns = [
    # path("", views.RecipeListView.as_view(), name="recipes-home"),
    path("", views.recipeListView, name="recipes-home"),
    path("<int:pk>/", views.recipeDetailView, name="recipes-detail"),
    path("new/", views.RecipeCreateForm, name="recipes-new"),
    path("my-recipes/", views.MyRecipeListView.as_view(), name="recipes-my"),

]