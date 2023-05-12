from django.http import HttpResponse
import random
from django.shortcuts import render

from .models import FootballPlayer

# Create your views here.

index_template = f"""
    <form action="/add_name/" method="POST">
        <div>
            <label for="new_item">Please enter the name of the player</label>
            <input name="name" id="new_item" value="" />
        </div>
    </form>
    
    <form action="/add_position/" method="POST">
        <div>
            <label for="new_item">Please specify the position of the player (e.g. GK, CB, CM, ST, LW, CAM)</label>
            <input name="position" id="new_position" value="" />
        </div>
    </form>
    
    <form action="/add_club/" method="POST">  
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
    </form>
    
    <form action="/add_fee/" method="POST">
        <div>
            <label for="new_item">Please specify transfer fee otherwise computer will do it for you</label>
            <input name="fee" id="new_item" value="" />
        </div>
            <button>Send my choice</button>
    </form>
"""


def index(request):
    return HttpResponse(index_template)


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
#                    f"Transfer fee {'(added by user): ' if user_input else '(random integer): '}{transfer_fee} millions euros"
#         print(response)
#         diary_footballplayer = FootballPlayer(name=name, position=position, club=club, transfer_fee=transfer_fee)
#         diary_footballplayer.save()
#     else:
#         response = "Please create a player"
#     return HttpResponse(response)

def add_name(request):
    if request.POST:
        name = request.POST.get("name")
        response = f"Player Name: {name}"
        diary_football_player = FootballPlayer(name=name)
        diary_football_player.save()
    else:
        response = "Please create a player"
    return HttpResponse(response)


def add_position(request):
    if request.POST:
        position = request.POST.get("position")
        response = f"Position on the field: {position}"
        diary_football_player = FootballPlayer(position=position)
        diary_football_player.save()
    else:
        response = "Please create a player"
    return HttpResponse(response)


def add_club(request):
    if request.POST:
        club = request.POST.get("club")
        response = f"Player club: {club}"
        diary_football_player = FootballPlayer(club=club)
        diary_football_player.save()
    else:
        response = "Please create a player"
    return HttpResponse(response)


def add_fee(request):
    if request.POST:
        user_input = False
        try:
            transfer_fee = int(request.POST.get('fee'))
            user_input = True
        except ValueError:
            transfer_fee = random.randrange(1, 100)
        response = f"Transfer fee {'(added by user): ' if user_input else '(random integer): '}{transfer_fee} millions euros"
        diary_football_player = FootballPlayer(transfer_fee=transfer_fee)
        diary_football_player.save()
    else:
        response = "Please create a player"
    return HttpResponse(response)

