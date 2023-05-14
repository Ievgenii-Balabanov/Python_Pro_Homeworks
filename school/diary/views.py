from django.http import HttpResponse
import random
from django.shortcuts import redirect
from django.shortcuts import render

from .models import FootballPlayer

index_template = f"""
    <form action="/login/" method="POST">
        <div>
            <label for="new_item">Please enter the name of the player</label>
            <input name="name" id="new_item" value="" />
        </div>
    
        <div>
            <label for="new_item">Please specify the position of the player (e.g. GK, CB, CMF, ST, LW, CAM)</label>
            <input name="position" id="new_position" value="" />
        </div>
        
        <fieldset>
            <legend>Please select your preferred football club:</legend>
            <div>
                <input type="radio" id="contactChoice1" name="contact" value="PSG"  />
                <label for="contactChoice1">PSG</label>
                <input type="radio" id="contactChoice2" name="contact" value="Parma" />
                <label for="contactChoice2">Parma</label>

                <input type="radio" id="contactChoice3" name="contact" value="Juventus" />
                <label for="contactChoice2">Juventus</label>
            </div>
        </fieldset>
        
        <div>
            <label for="new_item">Please specify transfer fee otherwise computer will do it for you</label>
            <input name="fee" id="new_item" value="" />
        </div>
            <button>Send my choice</button>
    </form>
"""

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
            </div>
        </fieldset>
        <p>
        <div>
            <label for="new_item">Specify new market value</label>
            <input name="fee" id="new_item" value=""/>
        </div>
        <p>
            <button>Send my choice</button>
        <p>
        <div>
            <a href="/">Return to the HOME page</a>
        </div>
    </form>
"""


user_pk = 4


def index(request):
    return HttpResponse(index_template)


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
                   f"Transfer fee {'(added by user): ' if user_input else '(random integer): '}{transfer_fee} millions euros"
        print(response)
        diary_football_player = FootballPlayer(name=name, position=position, club=club, transfer_fee=transfer_fee)
        diary_football_player.save()
    else:
        response = "Please create a player"
    return HttpResponse(response)


def is_exist_check(request):
    f"""
    функция проверяет существует ли инстанс с указанным pk и если нет - редирект на страницу формы
    """
    try:
        football_player = FootballPlayer.objects.get(pk=user_pk)
        return HttpResponse(football_player)
    except Exception:
        return redirect(index)


def param_update(request):
    if request.POST:
        football_player = FootballPlayer.objects.get(pk=user_pk)
        football_player.name = request.POST.get("name")
        football_player.position = request.POST.get("position")
        football_player.club = request.POST.get("contact")
        football_player.transfer_fee = int(request.POST.get('fee'))
        football_player.save()
    return HttpResponse(update_template)



# def param_update(request):
#     """
#         изменение параметров инстанса
#         :return:
#     """
#     football_player = FootballPlayer.objects.filter(name="Gatti").update(position="CB", club="Juventus")
#     return HttpResponse(f"Amount of updated instances: {football_player}")

    # #multiple update
    # my_footballplayer = FootballPlayer.objects.get(pk=19)
    # FootballPlayer.objects.update(position="GK")
    # return HttpResponse(my_footballplayer)
