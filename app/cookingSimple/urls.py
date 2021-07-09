from django.contrib import admin
from django.conf import settings
from users.views import profile
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path("", include("recipes.urls")),
    path("", include("allauth.urls")),
    path("", include("users.urls")),
    path("profile/", profile, name="users-profile"),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
