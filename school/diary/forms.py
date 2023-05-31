from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput

from .models import FootballPlayer


class FootballPlayerForm(ModelForm):
    class Meta:
        model = FootballPlayer
        fields = ["name", "position", "club", "transfer_fee"]

        widgets = {
            "name": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter the name"}
            ),
            "position": TextInput(
                attrs={"class": "form-control", "placeholder": "Specify the position"}
            ),
            "club": TextInput(
                attrs={"class": "form-control", "placeholder": "Select club"}
            ),
            "transfer_fee": TextInput(
                attrs={"class": "form-control", "placeholder": "Specify market value"}
            ),
        }

    # name = forms.CharField(min_length=2, max_length=30)
    # position = forms.CharField(min_length=2, max_length=5)
    # transfer_fee = forms.IntegerField()
    # club = forms.CharField(max_length=13)

    def clean_name(self):
        name_data = self.cleaned_data["name"]
        if name_data.islower():
            raise ValidationError("Name is to short. Use at least 2 symbols")
        return name_data

    def clean_position(self):
        position_data = self.cleaned_data["position"]
        if not position_data.isupper():
            raise ValidationError("Please use only upper case letters")
        return position_data

    def clean_club(self):
        club_data = self.cleaned_data["club"]
        if club_data.islower():
            raise ValidationError("Data is out of range or lower case only")
        return club_data

    def clean_transfer_fee(self):
        transfer_fee_data = self.cleaned_data["transfer_fee"]
        if transfer_fee_data not in range(1, 151):
            raise ValidationError("Data is out of range or lower case only")
        return transfer_fee_data

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        position = cleaned_data.get("position")

        if name == position:
            self.add_error("name", "Name is to short. Use at least 2 symbols")


class AchievementForm(forms.Form):
    tournament = forms.CharField(min_length=3, max_length=25)
    achievement = forms.CharField(min_length=5, max_length=200)
    scored_goals = forms.IntegerField(min_value=0, max_value=200)
    appearances = forms.IntegerField(min_value=1)
    clean_sheets = forms.IntegerField(required=False)

    def __init__(self, *args, **kwargs):
        self._football_player_id = kwargs.pop("football_player_id")
        super().__init__(*args, **kwargs)

    def clean_tournament(self):
        tournament_data = self.cleaned_data["tournament"]
        if len(tournament_data.split(" ")) < 2:
            raise ValidationError(
                "Please specify a Tournament name " "that consists of at least 2 words!"
            )
        return tournament_data

    def clean_achievement(self):
        achievement_data = self.cleaned_data["achievement"]
        if len(achievement_data.split(" ")) < 2:
            raise ValidationError(
                "Please specify achievement " "that consists of at least 2 words!"
            )
        return achievement_data

    def clean_appearances(self):
        appearances_data = self.cleaned_data["appearances"]
        if appearances_data < 5:
            raise ValidationError(
                "Minimum allowable quantity "
                "of the appearances in the season "
                "must be more then 5"
            )
        return appearances_data

    def clean_scored_goals(self):
        scored_goals_data = self.cleaned_data["scored_goals"]
        if scored_goals_data < 0:
            raise ValidationError("Allowed number of scored goals must be zero or more")
        return scored_goals_data

    def clean_clean_sheets(self):
        clean_sheets_data = self.cleaned_data["clean_sheets"]
        football_player = FootballPlayer.objects.get(pk=self._football_player_id)
        if clean_sheets_data and football_player.position != "GK":
            raise ValidationError(
                "Incorrect position is specified. "
                '"Clean sheets" field is allowed '
                'only for the "GK" position'
            )
        return clean_sheets_data

    def clean(self):
        cleaned_data = super().clean()
        achievement = cleaned_data.get("achievement")
        appearances = cleaned_data.get("appearances")

        if not (appearances and achievement):
            self.add_error(
                "appearances",
                "Note: both fields "
                '"Appearances" '
                'and "Achievement" '
                "are required",
            )
