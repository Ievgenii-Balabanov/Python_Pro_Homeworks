from django.db import models


class User(models.Model):
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=25)


class FootballPlayer(models.Model):
    """
    класс FootballPlayer хранящий параметры для создания инстанса
    """
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=5, null=True)
    transfer_fee = models.IntegerField(default=0)
    club = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        return f"Name: {self.name}, Position: {self.position}, Club: {self.club}, " \
               f"Market value: {self.transfer_fee} million(s) euros"


def validate_isalpha(form_input):
    """
    валидация являются ли вводимые значения символами
    :param form_input:
    :return:
    """
    if form_input.isalpha() and 0 < len(form_input) < 21:
        return form_input
    return Exception("Data isn't alpha or out of range")


def validate_isupper(form_input):
    """
       проеврка что вводимые значения используют символы исключительно верхнего регистра,
       и длина инпута соответствует заданным параметрам
       :param form_input:
       :return:
       """
    if form_input.isalpha() and 1 < len(form_input) < 5 and form_input.isupper():
        return form_input
    return Exception("Position data isn't correct!")


def validate_isdigit(form_input):
    """
        валидация являются ли вводимые значения цифрами
        :param form_input:
        :return:
        """
    try:
        form_input = int(form_input)
        if form_input > 0:
            return form_input
        return Exception("Fee value isn't correct!")
    except ValueError:
        return "Data value isn't correct!"


class Achievement(models.Model):
    football_player_achievements = models.ForeignKey(FootballPlayer, on_delete=models.CASCADE)
    tournament = models.CharField(max_length=100)
    achievement = models.CharField(max_length=250)
    scored_goals = models.IntegerField(default=0)
    appearances = models.IntegerField(default=0)
    clean_sheets = models.IntegerField(null=True)

