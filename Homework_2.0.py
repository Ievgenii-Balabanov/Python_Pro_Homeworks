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
        if type(param) == str:
            # я не нашел такого метода
            if param.isascii():
                return param
            return Exception("String is not ascii!")


def validate_alphabetical(form_input, error_key, error_dict=None):
    if form_input.isalpha():
        return form_input
    error_dict[error_key] = "Verbose error description"


@app.route("/login", methods=["GET", "POST"])
def login_player():
    error_dict = {}

    name = validate_alphabetical(request.form.get("name"), "name", error_dict)
    position = request.form.get("position")

    if error_dict:
        return f"""
            {error_dict['name']}
        """

    try:
        global player
        player = FootballPlayer(name, position)
        return redirect("/")
    except:
        return f"""
            Name or position is not in ascii
        """


@app.route("/")
def display_info():
    return f"""
        <h1>Football player information: {player.name, player.position, player.club, player.transfer_fee}</h1>

        <form action="/add_name" method="POST">
            <div>
                <label for="new_item">Please enter the name of the player</label>
                <input name="item" id="new_item" value="Enter the name" />
            </div>
                <button>Submit</button>
        </form>

        <form action="/add_position" method="POST">
            <div>
                <label for="new_item">Please specify the position of the player (e.g. GK, CB, CM, ST, LW, CAM)</label>
                <input name="item" id="new_item" value="Specify the position" />
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
    item = request.form.get('item')
    player.name = item
    return f"""
    <h3>Player information: {player.name, player.position, player.club, player.transfer_fee}</h3>
    <h4>Name: {item}</h4>
    </br>
    <a href="/">Return to the HOME page</a>
    """


@app.route("/add_position", methods=["POST"])
def add_position():
    item = request.form.get('item')
    player.position = item
    return f"""
        <h3>Player position: {player.name, player.position, player.club, player.transfer_fee}</h3>
        <h4>Position: {item}</h4>

        </br>
        <a href="/">Return to the HOME page</a>
    """


@app.route("/add_club", methods=["POST"])
def add_club():
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
    user_input = False
    try:
        item = int(request.form.get('item'))
        user_input = True
    except ValueError:
        item = randint(1, 100)
    player.transfer_fee = str(item)

    return f"""
        <h3>Football player information: {player.name, player.position, player.club, player.transfer_fee}</h3>
        </br>
        <h4>Transfer fee {'(added by user): ' if user_input else '(random integer): '}{item} millions euros</h4>
        </br>
        <a href="/">Return to the HOME page</a>
    """


player = FootballPlayer(name="", position="")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

