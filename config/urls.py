
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += i18n_patterns(
    path("", views.home, name="home"),
    path("a-propos/", views.apropos, name="apropos"),
    path("expertises/", views.expertises, name="expertises"),
    path("notre-approche/", views.approche, name="approche"),
    path("implantations/", views.implantations, name="implantations"),
    prefix_default_language=False,
)
