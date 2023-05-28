import pytest
from django.urls import reverse
from pytest_django.asserts import assertQuerysetEqual

from .models import FootballPlayer, Achievement


# check is redirection works correctly
@pytest.mark.urls("school.urls")
def test_is_exist_redirect(client):
    """
    testing status_code matching
    :param client:
    :return:
    """
    response = client.get("/is_exist_check/")
    assert response.status_code == 302


@pytest.mark.urls("school.urls")
def test_is_exist_redirects_to_root(client):
    """
    testing status_code matching and routing
    :param client:
    :return:
    """
    response = client.get("/is_exist_check/")
    assert response.status_code == 302
    assert response.url == reverse("index")


# --------------------------------------------------------------------------------

# @pytest.mark.django_db
# def test_new_player_add(client):
#     """
#     simple test add player
#     :param client:
#     :return:
#     """
#     response_clean_database = client.get('/football_player/')
#     football_players = FootballPlayer.objects.all()
#     assertQuerysetEqual(response_clean_database.context["players"],
#                         football_players)
#     new_db_player_name = "Gattuso"
#     new_db_player_position = "CMF",
#     new_db_player_club = "Valencia",
#     new_db_player_transfer_fee = 12
#     FootballPlayer.objects.create(name=new_db_player_name,
#                                   position=new_db_player_position,
#                                   club=new_db_player_club,
#                                   transfer_fee=new_db_player_transfer_fee)
#     football_players_updated = FootballPlayer.objects.all()
#     response_fulfilled_database = client.get('/football_player/')
#     assertQuerysetEqual(response_fulfilled_database.context['players'],
#                         football_players_updated, ordered=False)
#     assert len(response_fulfilled_database.context['players']) == 1

# --------------------------------------------------------------------------------


@pytest.mark.django_db
def test_new_player_add_and_achievements(client, football_player_achievements_id=None):
    """
    Test failed attempt to add one player and achievements to it
    :param client:
    :param football_player_achievements_id:
    :return:
    """
    response_clean_database = client.get("/football_player/")
    football_players = FootballPlayer.objects.all()
    assertQuerysetEqual(response_clean_database.context["players"], football_players)
    new_db_player_name = "Gattuso"
    new_db_player_position = ("CMF",)
    new_db_player_club = ("Valencia",)
    new_db_player_transfer_fee = 12
    FootballPlayer.objects.create(
        name=new_db_player_name,
        position=new_db_player_position,
        club=new_db_player_club,
        transfer_fee=new_db_player_transfer_fee,
    )

    new_tournament = "Seria A"
    new_achievement = "3X Seria A winner"
    new_scored_goals = 4
    new_appearances = 378
    new_clean_sheets = 0
    Achievement.objects.create(
        football_player_achievements_id=1,
        tournament=new_tournament,
        achievement=new_achievement,
        scored_goals=new_scored_goals,
        appearances=new_appearances,
        clean_sheets=new_clean_sheets,
    )
    football_players_updated = FootballPlayer.objects.all()
    # achievements_updated = Achievement.objects.all()
    response_fulfilled_database = client.get("/football_player/")
    # new_response_fulfilled_database = client.get('/football_player/1/')
    assertQuerysetEqual(
        response_fulfilled_database.context["players"],
        football_players_updated,
        ordered=False,
    )
    assert len(response_fulfilled_database.context["players"]) == 1

    # @pytest.mark.django_db
    # def test_new_achievement_add(client):
    #     response = client.get('football_player/1/add_achievement/')
    #     certain_player = FootballPlayer.objects.get(name="Gattuso")
    #     assertQuerysetEqual(response, certain_player)
    #     new_tournament = "Seria A"
    #     new_achievement = "3X Seria A winner"
    #     new_scored_goals = 4
    #     new_appearances = 378
    #     new_clean_sheets = 0
    # Achievement.objects.create(
    #     tournament=new_tournament,
    #     achievement=new_achievement,
    #     scored_goals=new_scored_goals,
    #     appearances=new_appearances,
    #     clean_sheets=new_clean_sheets,
    # )


#     players_updated = Achievement.objects.all()
#     response_updated = client.get('football_player/1/add_achievement/')
#     assertQuerysetEqual(response_updated, players_updated)
