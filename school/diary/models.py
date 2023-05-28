from django.db import models


class FootballPlayer(models.Model):
    """
    класс FootballPlayer хранящий параметры для создания инстанса
    """
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=5, null=True)
    club = models.CharField(max_length=25, null=True, blank=True)
    transfer_fee = models.IntegerField()

    def __str__(self):
        return f"Name: {self.name}, Position: {self.position}, " \
               f"Club: {self.club}, " \
               f"Market value: {self.transfer_fee} million(s) euros"


class Achievement(models.Model):
    football_player_achievements = \
        models.ForeignKey(FootballPlayer, on_delete=models.CASCADE)
    tournament = models.CharField(max_length=100)
    achievement = models.CharField(max_length=250)
    scored_goals = models.IntegerField(default=0)
    appearances = models.IntegerField(default=0)
    clean_sheets = models.IntegerField(null=True, blank=True)
