from django.db import models


class FootballPlayer(models.Model):
    """
    класс FootballPlayer хранящий 4 параметра для создания инстанса
    """
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=5, null=True)
    transfer_fee = models.IntegerField(default=0)
    club = models.CharField(max_length=3, null=True, blank=True)


def validate_isalpha(form_input):
    """
    валидация являются ли вводимые значения символами
    :param form_input:
    :return:
    """
    if form_input.isalpha() and 1 < len(form_input) < 21:
        return form_input
    return Exception("Incorrect data")


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


"""
некоторые проверки кооректной работы валидаторов
"""
# print(validate_isalpha("@#")) # --> must be NOT ok
# print(validate_isalpha("123")) # --> must be NOT ok
# print(validate_isalpha("qwert")) # --> must be ok
# print(validate_isalpha("aaaaa")) # --> must be ok
# print(validate_isalpha("aaaaaaaaaaaaaaaaaaaaa")) # --> must be NOT ok
# print(validate_isalpha("aaaaaaaaaaaaaaaaaaaaaaaa")) # --> must be NOT ok
# print(validate_isupper("QQQQ")) # --> must be ok
# print(validate_isdigit(1)) # --> must be ok
# print(validate_isdigit(-123)) # --> must be NOT ok
# print(validate_isdigit("qwerty")) # --> must be NOT ok
