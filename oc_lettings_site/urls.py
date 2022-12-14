from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("lettings/", include(("lettings.urls", "lettings"), namespace="lettings")),
    path("profiles/", include(("profiles.urls", "profiles"), namespace="profiles")),
    path("admin/", admin.site.urls),
    path('sentry-debug/', views.trigger_error),
]
