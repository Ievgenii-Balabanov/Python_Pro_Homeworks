from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("param_update/", views.param_update, name="param_update"),
    path("is_exist_check/", views.is_exist_check, name="is_exist_check"),
    path("football_player/", views.football_player, name="football_player"),
    path("football_player/<int:football_player_id>/", views.footballer, name="player"),
    path(
        "football_player/<int:football_player_id>/add_achievement/",
        views.add_achievement,
        name="new_achievement",
    ),
    path(
        "achievement/<achievement_id>/", views.achievements_detail, name="achievement"
    ),
]
