from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader

from .forms import AchievementForm, FootballPlayerForm
from .models import FootballPlayer
from .models import Achievement

player = None


def index(request):
    error = ""
    if request.POST:
        form_data = FootballPlayerForm(request.POST)
        if form_data.is_valid():
            some_new_player = \
                FootballPlayer.objects.create(
                    name=form_data.cleaned_data['name'],
                    position=form_data.cleaned_data['position'],
                    club=form_data.cleaned_data['club'],
                    transfer_fee=form_data.cleaned_data['transfer_fee'], )
            global player
            player = some_new_player.id
            print(player)
        else:
            error = "Please enter valid data!"

    form_data = FootballPlayerForm

    data = {
        'form': form_data,
        'error': error
    }

    return render(request, 'diary/index.html', data)


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
    """
    функция проверяет существует ли инстанс
    с указанным pk и если нет - редирект на страницу формы
    :param request:
    :return:
    """
    try:
        some_player = FootballPlayer.objects.get(pk=player)
        return HttpResponse(some_player)
    except Exception:
        return redirect(index)


def param_update(request):
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
    return render(request, "diary/achievements_detail.html",
                  {"achievement_key": reaching})


def add_achievement(request, football_player_id):
    if request.POST:
        if not player:
            return redirect(index)
    new_player = get_object_or_404(FootballPlayer, pk=football_player_id)
    form_data = AchievementForm(request.POST,
                                football_player_id=football_player_id)
    if form_data.is_valid():
        Achievement.objects. \
            create(football_player_achievements=new_player,
                   tournament=form_data.cleaned_data['tournament'],
                   achievement=form_data.cleaned_data['achievement'],
                   scored_goals=form_data.cleaned_data['scored_goals'],
                   appearances=form_data.cleaned_data['appearances'],
                   clean_sheets=form_data.cleaned_data['clean_sheets'], )

    return render(request, "diary/player.html",
                  {"players": new_player,
                   "error_message": form_data.errors})


print(player)
