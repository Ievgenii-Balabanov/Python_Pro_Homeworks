from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("param_update/", views.param_update, name="param_update"),
    path("is_exist_check/", views.is_exist_check, name="is_exist_check"),
]
