from django.urls import path, include
from .views import (
    favourite_add,
    favourite_list,
)

urlpatterns = [
    path("fav/<int:pk>", favourite_add, name="favourite-add"),
    path("profile/favourites/", favourite_list, name="favourite-list"),
    
]