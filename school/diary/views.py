from django.http import HttpResponse
import random
from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader

from .forms import AchievementForm
from .models import FootballPlayer, User
from .models import Achievement
from django.template.loader import render_to_string

player = None


def index(request):
    return render(request, "diary/index.html")
# def index(request):
#     return render(request, "diary/login.html")


# def add_user(request):
#     if request.POST:
#         login = request.POST.get("login")
#         password = request.POST.get("password")
#         response = f"Player Name: {login}, Position: {password}

# ----------------------------------------------------------------


def login(request):
    if request.POST:
        name = request.POST.get("name")
        position = request.POST.get("position")
        club = request.POST.get("contact")
        user_input = False
        try:
            transfer_fee = int(request.POST.get('fee'))
            user_input = True
        except ValueError:
            transfer_fee = random.randrange(1, 100)
        response = f"Player Name: {name}, Position: {position}, Club: {club}, " \
                   f"Transfer fee {'(added by user): ' if user_input else '(random integer): '}" \
                   f"{transfer_fee} millions euros"

        some_player = FootballPlayer.objects.create(name=name, position=position, club=club, transfer_fee=transfer_fee)
        global player
        player = some_player.id
        print(player)
    else:
        response = "Please create a player"

    return HttpResponse(response)


# ----------------------------------------------------------------


# def login(request):
#     global player
#     if request.POST:
#         login = request.POST.get("login")
#         password = request.POST.get("password")
#         response = f"Player Name: {login}, Position: {password}"
#         new_user = User.objects.create(login=login, password=password)
#         player = new_user.id
#     else:
#         response = "To get started, log in to the system!"
#     return HttpResponse(response)
#
#
# def player_registration(request):
#     if request.POST:
#         name = request.POST.get("name")
#         position = request.POST.get("position")
#         club = request.POST.get("contact")
#         user_input = False
#         try:
#             transfer_fee = request.POST.get('fee')
#             user_input = True
#         except ValueError:
#             transfer_fee = random.randrange(1, 100)
#         response = f"Player Name: {name}, Position: {position}, Club: {club}, " \
#                    f"Transfer fee {'(added by user): ' if user_input else '(random integer): '}" \
#                    f"{transfer_fee} millions euros"
#
#         some_player = FootballPlayer.objects.create(name=name, position=position, club=club, transfer_fee=transfer_fee)
#         global player
#         player = some_player.id
#         # print(player)
#     else:
#         response = "Please create a player"
#
#     return HttpResponse(response)

#
def add_achievements(request):
    """
        вносим достижения инстанса
        :return:
        """
    if request.POST:
        if not player:
            return redirect("login")
        achievements = request.POST.get("achievements")
        response = f"Player club: {achievements}"
        diary_football_player = FootballPlayer(achievements=achievements)
        diary_football_player.save()
    else:
        response = "Please create a player"
    return HttpResponse(response)


def is_exist_check(request):
    f"""
    функция проверяет существует ли инстанс с указанным pk и если нет - редирект на страницу формы
    """
    try:
        some_player = FootballPlayer.objects.get(pk=player)
        return HttpResponse(some_player)
    except Exception:
        return redirect(index)


def param_update(request):
    template = loader.get_template("diary/player_update.html")
    if request.POST:
        football_player = FootballPlayer.objects.get(pk=player)
        football_player.name = request.POST.get("name")
        football_player.position = request.POST.get("position")
        football_player.club = request.POST.get("contact")
        football_player.transfer_fee = int(request.POST.get('fee'))
        football_player.achievements = request.POST.get("achievements")
        football_player.save()
    return render(request, "diary/player_update.html")


def football_player(request):
    template = loader.get_template("diary/info_football_player.html")
    context = {
        "players": FootballPlayer.objects.all()
    }
    return HttpResponse(template.render(context, request))


def footballer(request, football_player_id):
    player = get_object_or_404(FootballPlayer, pk=football_player_id)
    return render(request, "diary/player.html", {"players": player})


def achievements(request):
    ach_template = loader.get_template("diary/achievements_detail.html")
    context_achievement = {
        "achievement_key": Achievement.objects.all()
    }
    return HttpResponse(ach_template.render(context_achievement, request))


def achievements_detail(request, achievement_id):
    reaching = get_object_or_404(Achievement, pk=achievement_id)
    return render(request, "diary/achievements_detail.html", {"achievement_key": reaching})


def add_achievement(request, football_player_id):
    if request.POST:
        if not player:
            return redirect(login)
    new_player = get_object_or_404(FootballPlayer, pk=football_player_id)
    form_data = AchievementForm(request.POST, football_player_id=football_player_id)
    if form_data.is_valid():
        Achievement.objects.create(football_player_achievements=new_player,
                                   tournament=form_data.cleaned_data['tournament'],
                                   achievement=form_data.cleaned_data['achievement'],
                                   scored_goals=form_data.cleaned_data['scored_goals'],
                                   appearances=form_data.cleaned_data['appearances'],
                                   clean_sheets=form_data.cleaned_data['clean_sheets'],)

    return render(request, "diary/player.html", {"players": new_player, "error_message": form_data.errors})
print(player)
