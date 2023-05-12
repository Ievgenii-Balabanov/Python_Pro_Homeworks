from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_name/", views.add_name, name="add_name"),
    path("add_position/", views.add_position, name="add_position"),
    path("add_club/", views.add_club, name="add_club"),
    path("add_fee/", views.add_fee, name="add_fee"),
]
