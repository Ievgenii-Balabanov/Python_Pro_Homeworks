import pytest
from django.urls import reverse
from pytest_django.asserts import assertQuerysetEqual

from .models import FootballPlayer, Achievement


@pytest.mark.urls('school.urls')
def test_is_exist_redirect(client):
    """
    testing status_code matching
    :param client:
    :return:
    """
    some_url = reverse("is_exist_check")
    response = client.get(some_url)
    assert response.status_code == 302


@pytest.mark.urls('diary.urls')
def test_is_exist_redirects_to_root(client):
    """
    testing status_code matching and routing
    :param client:
    :return:
    """

    some_url = reverse("is_exist_check")
    response = client.get(some_url)
    assert response.status_code == 302
    assert response.url == reverse('index')

# --------------------------------------------------------------------------------


@pytest.mark.django_db
def test_new_player_add(client):
    """
    simple test add player
    :param client:
    :return:
    """
    football_player_url = reverse("football_player")
    response_clean_database = client.get(football_player_url)
    football_players = FootballPlayer.objects.all()
    new_db_player_name = "Gattuso"
    new_db_player_position = "CMF",
    new_db_player_club = "Valencia",
    new_db_player_transfer_fee = 12
    FootballPlayer.objects.create(name=new_db_player_name,
                                  position=new_db_player_position,
                                  club=new_db_player_club,
                                  transfer_fee=new_db_player_transfer_fee)
    football_players_updated = FootballPlayer.objects.all()
    response_fulfilled_database = client.get(football_player_url)
    assertQuerysetEqual(response_fulfilled_database.context['players'],
                        football_players_updated, ordered=False)
    assert len(response_fulfilled_database.context['players']) == 1

# --------------------------------------------------------------------------------


# @pytest.mark.django_db
# def test_new_achievement_add(client):
#     add_achievement_url = reverse("new_achievement")
#     response = client.get(add_achievement_url)
#     certain_player = FootballPlayer.objects.all()
#     assertQuerysetEqual(response, certain_player)
#     new_tournament = "Seria A"
#     new_achievement = "3X Seria A winner"
#     new_scored_goals = 4
#     new_appearances = 378
#     new_clean_sheets = 0
#     Achievement.objects.create(tournament=new_tournament,
#                                achievement=new_achievement,
#                                scored_goals=new_scored_goals,
#                                appearances=new_appearances,
#                                clean_sheets=new_clean_sheets)
#     players_updated = Achievement.objects.all()
#     response_updated = client.get('football_player/1/add_achievement/')
#     assertQuerysetEqual(response_updated, players_updated)

@pytest.mark.django_db
def test_new_achievement_add(client):
    # url_some = reverse("new_achievement")
    football_player_id = FootballPlayer.objects.all()
    # response = client.get(url_some)
    response = client.get('football_player/1/add_achievement/')
    certain_player = FootballPlayer.objects.all()
    assertQuerysetEqual(response, certain_player)
    football_player_id = 2
    new_tournament = "Seria A"
    new_achievement = "3X Seria A winner"
    new_scored_goals = 4
    new_appearances = 378
    new_clean_sheets = 0
    Achievement.objects.create(football_player_id=2, tournament=new_tournament, achievement=new_achievement, scored_goals=new_scored_goals,
                               appearances=new_appearances, clean_sheets=new_clean_sheets)
    players_updated = Achievement.objects.all()
    response_updated = client.get('football_player/1/add_achievement/')
    assertQuerysetEqual(response_updated, players_updated)
