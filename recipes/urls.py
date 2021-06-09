from django.urls import path, include
from .views import (
    RecipesCreateFormView,
    RecipesListView,
    RecipesDetailView,
    RecipesCreateView,
    RecipesCreateFormView,
    FormSuccessView,
)

urlpatterns = [
    path("", RecipesListView.as_view(), name="recipes-home"),
    path("<int:pk>/", RecipesDetailView.as_view(), name="recipes-detail"),
    path("new/", RecipesCreateFormView.as_view(), name="recipes-new"),
]