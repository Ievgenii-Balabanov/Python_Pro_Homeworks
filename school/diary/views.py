from django.http import HttpResponse
import random
from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader

from .forms import AchievementForm
from .models import FootballPlayer
from .models import Achievement
from django.template.loader import render_to_string

player = None

# index_template = f"""
#     <form action="/login/" method="POST">
#         <div>
#             <label for="new_item">Please enter the name of the player</label>
#             <input name="name" id="new_item" value="" />
#         </div>
#
#         <div>
#             <label for="new_item">Please specify the position of the player (e.g. GK, CB, CMF, ST, LW, CAM)</label>
#             <input name="position" id="new_position" value="" />
#         </div>
#
#         <fieldset>
#             <legend>Please select your preferred football club:</legend>
#             <div>
#                 <input type="radio" id="contactChoice1" name="contact" value="PSG"  />
#                 <label for="contactChoice1">PSG</label>
#                 <input type="radio" id="contactChoice2" name="contact" value="Parma" />
#                 <label for="contactChoice2">Parma</label>
#                 <input type="radio" id="contactChoice3" name="contact" value="Juventus" />
#                 <label for="contactChoice3">Juventus</label>
#                 <input type="radio" id="contactChoice3" name="contact" value="Milan" />
#                 <label for="contactChoice4">Milan</label>
#                 <input type="radio" id="contactChoice3" name="contact" value="Barcelona" />
#                 <label for="contactChoice5">Barcelona</label>
#                 <input type="radio" id="contactChoice3" name="contact" value="Real Madrid" />
#                 <label for="contactChoice6">Real Madrid</label>
#             </div>
#         </fieldset>
#
#         <div>
#             <label for="new_item">Please specify transfer fee otherwise computer will do it for you</label>
#             <input name="fee" id="new_item" value="" />
#         </div>
#
#         <div>
#             <label for="new_item">Specify achievements</label>
#             <input name="achievements" id="new_item" value="" />
#         </div>
#             <button>Send my choice</button>
#     </form>
# """

update_template = f"""
    <form action="/param_update/" method="POST">
        <div>
            <label for="new_item">Enter new name of the player</label>
            <input name="name" id="new_item" value="" />
        </div>
        <p>
        <div>
            <label for="new_item">Please specify the position of the player (e.g. GK, CB, CMF, ST, LW, CAM)</label>
            <input name="position" id="new_position" value="" />
        </div>
        <p>
        <fieldset>
            <legend>Select new football club:</legend>
            <div>
                <input type="radio" id="contactChoice1" name="contact" value="PSG"  />
                <label for="contactChoice1">PSG</label>
                <input type="radio" id="contactChoice2" name="contact" value="Parma" />
                <label for="contactChoice2">Parma</label>
                <input type="radio" id="contactChoice3" name="contact" value="Juventus" />
                <label for="contactChoice2">Juventus</label>
                <input type="radio" id="contactChoice3" name="contact" value="Milan" />
                <label for="contactChoice4">Milan</label>
                <input type="radio" id="contactChoice3" name="contact" value="Barcelona" />
                <label for="contactChoice5">Barcelona</label>
                <input type="radio" id="contactChoice3" name="contact" value="Real Madrid" />
                <label for="contactChoice6">Real Madrid</label>
            </div>
        </fieldset>
        <p>
        <div>
            <label for="new_item">Specify new market value</label>
            <input name="fee" id="new_item" value=""/>
        </div>
        <p>
        <div>
            <label for="new_item">Specify achievements</label>
            <input name="achievements" id="new_item" value="" />
        </div>
        <p>
            <button>Send my choice</button>
        <p>
        <div>
            <a href="/">Return to the HOME page</a>
        </div>
    </form>
"""


def index(request):
    return render(request, "diary/index.html")


# def login(request):
#     if request.POST:
#         name = request.POST.get("name")
#         position = request.POST.get("position")
#         club = request.POST.get("contact")
#         user_input = False
#         try:
#             transfer_fee = int(request.POST.get('fee'))
#             user_input = True
#         except ValueError:
#             transfer_fee = random.randrange(1, 100)
#         response = f"Player Name: {name}, Position: {position}, Club: {club}, " \
#                    f"Transfer fee {'(added by user): ' if user_input else '(random integer): '}" \
#                    f"{transfer_fee} millions euros"
#
#         diary_football_player = FootballPlayer(name=name, position=position, club=club, transfer_fee=transfer_fee)
#         diary_football_player.save()
#     else:
#         response = "Please create a player"
#     return HttpResponse(response)

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
    else:
        response = "Please create a player"
    return HttpResponse(response)


def add_achievements(request):
    """
        вносим достижения инстанса
        :return:
        """
    if request.POST:
        achievements = request.POST.get("achievements")
        response = f"Player club: {achievements}"
        diary_football_player = FootballPlayer(achievements=achievements)
        diary_football_player.save()
    else:
        response = "Please create a player"
    return HttpResponse(response)


# def is_exist_check(request):
#     f"""
#     функция проверяет существует ли инстанс с указанным pk и если нет - редирект на страницу формы
#     """
#     try:
#         football_player = FootballPlayer.objects.get(pk=4)
#         return HttpResponse(football_player)
#     except Exception:
#         return redirect(index)

def is_exist_check(request):
    f"""
    функция проверяет существует ли инстанс с указанным pk и если нет - редирект на страницу формы
    """
    try:
        some_player = FootballPlayer.objects.get(pk=pk)
        return HttpResponse(some_player)
    except Exception:
        return redirect(index)


def param_update(request):
    if request.POST:
        football_player = FootballPlayer.objects.get(pk=3)
        football_player.name = request.POST.get("name")
        football_player.position = request.POST.get("position")
        football_player.club = request.POST.get("contact")
        football_player.transfer_fee = int(request.POST.get('fee'))
        football_player.achievements = request.POST.get("achievements")
        football_player.save()
    return HttpResponse(update_template)


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
    player = get_object_or_404(FootballPlayer, pk=football_player_id)
    form_data = AchievementForm(request.POST)
    if form_data.is_valid():
        Achievement.objects.create(football_player_achievements=player,
                                   tournament=form_data.cleaned_data['tournament'],
                                   achievement=form_data.cleaned_data['achievement'],
                                   scored_goals=form_data.cleaned_data['scored_goals'],
                                   appearances=form_data.cleaned_data['appearances'],
                                   clean_sheets=form_data.cleaned_data['clean_sheets'],)

    return render(request, "diary/player.html", {"players": player, "error_message": form_data.errors})
