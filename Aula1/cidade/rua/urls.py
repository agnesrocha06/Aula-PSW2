from django.urls import path

from . import views

urlpatterns = [
    path("barbie/", views.index, name="index"),
]
