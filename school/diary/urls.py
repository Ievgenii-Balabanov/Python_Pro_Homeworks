from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_name/", views.add_name, name="name"),
    path("add_position/", views.add_position, name="position"),
    path("add_club/", views.add_club, name="club"),
    path("add_fee/", views.add_fee, name="transfer_fee"),
    path("footballer/", views.football_player, name="football_player")
]
