from flask import Flask, request, redirect
from random import randint

app = Flask(__name__)

player = None


class FootballPlayer:
    name = ""
    position = ""
    club = ""
    transfer_fee = ""

    def __init__(self, name, position):
        self.name = self.check_ascii(name)
        self.position = self.check_ascii(position)

    def check_ascii(self, param):
        if isinstance(param, str) and param.isascii():
            return param
        return Exception(f"Expected ascii string, received: {param}")


def validate_isalpha(form_input):
    """
    валидация являются ли вводимые значения символами
    :param form_input:
    :return:
    """
    if form_input.isalpha() and 1 < len(form_input) < 21:
        return form_input
    return Exception("Isn't alpha")


def validate_isupper(form_input):
    if form_input.isalpha() and 1 < len(form_input) < 5 and form_input.isupper():
        return form_input
    return Exception("Position data isn't correct!")


def validate_isdigit(form_input):
    try:
        form_input = int(form_input)
        if form_input > 0:
            return form_input
        return Exception("Fee value isn't correct!")
    except ValueError:
        return "Data value isn't correct!"



@app.route("/")
def display_info():
    return f"""
        <h1>Football player information: {player.name, player.position, player.club, player.transfer_fee}</h1>

        <form action="/add_name" method="POST">
            <div>
                <label for="new_item">Please enter the name of the player</label>
                <input name="name" id="new_item" value="" />
            </div>
                <button>Submit</button>
        </form>

        <form action="/add_position" method="POST">
            <div>
                <label for="new_item">Please specify the position of the player (e.g. GK, CB, CM, ST, LW, CAM)</label>
                <input name="position" id="new_position" value="" />
            </div>
                <button>Submit</button>
        </form>

        <form action ="add_club" method="POST">
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
                <div>
                    <button>Submit</button>
                </div>
            </fieldset>
        </form>

        <form action="/add_fee" method="POST">
            <div>
                <label for="new_item">Please specify your estimated transfer fee of the player or the computer will do it for you </label>
                <input name="item" id="new_item" value="random int" />
            </div>
                <button>Send my choice</button>
        </form>
    """


@app.route("/add_name", methods=["POST"])
def add_name():
    """
    присваиваем имя инстанса
    :return:
    """
    item_name = request.form.get('name')
    player.name = item_name
    return f"""
    <h3>Player information: {player.name, player.position, player.club, player.transfer_fee}</h3>
    <h4>Name: {item_name}</h4>
    </br>
    <a href="/">Return to the HOME page</a>
    """


@app.route("/add_position", methods=["POST"])
def add_position():
    """
    присваиваем позицию инстанса
    :return:
    """
    item_position = request.form.get('position')
    player.position = item_position
    return f"""
        <h3>Player position: {player.name, player.position, player.club, player.transfer_fee}</h3>
        <h4>Position: {item_position}</h4>
        </br>
        <a href="/">Return to the HOME page</a>
    """


@app.route("/add_club", methods=["POST"])
def add_club():
    """
    устанавливаем клуб инстанса
    :return:
    """
    try:
        contact = request.form.get('contact')
        player.club = contact
    except ValueError:
        print("Please specify the club")
    return f"""
        <h3>Player information: {player.name, player.position, player.club, player.transfer_fee}</h3>
        <h4>Club: {contact}</h4>

        </br>
        <a href="/">Return to the HOME page</a>
    """


@app.route("/add_fee", methods=["POST"])
def add_fee():
    """
    присваиваем возможную рыночную стоимость инстанса
    :return:
    """
    user_input = False
    try:
        item_fee = int(request.form.get('item'))
        user_input = True
    except ValueError:
        item_fee = randint(1, 100)
    player.transfer_fee = str(item_fee)

    return f"""
        <h3>Football player information: {player.name, player.position, player.club, player.transfer_fee}</h3>
        </br>
        <h4>Transfer fee {'(added by user): ' if user_input else '(random integer): '}{item_fee} millions euros</h4>
        </br>
        <a href="/">Return to the HOME page</a>
    """


player = FootballPlayer(name="", position="")


"""
некоторые проверки кооректной работы валидаторов
"""
print(player.check_ascii("Some text")) # --> must be ok
print(player.check_ascii(111)) # --> must be NOT ok
print(validate_isalpha("@#")) # --> must be NOT ok
print(validate_isalpha("123")) # --> must be NOT ok
print(validate_isalpha("qwert")) # --> must be ok
print(validate_isalpha("aaaaa")) # --> must be ok
print(validate_isalpha("aaaaaaaaaaaaaaaaaaaaa")) # --> must be NOT ok
print(validate_isalpha("aaaaaaaaaaaaaaaaaaaaaaaa")) # --> must be NOT ok
print(validate_isupper("QQQQ")) # --> must be ok
print(validate_isdigit(1)) # --> must be ok
print(validate_isdigit(-123)) # --> must be NOT ok
print(validate_isdigit("qwerty")) # --> must be NOT ok

#
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

