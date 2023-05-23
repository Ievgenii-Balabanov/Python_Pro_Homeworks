from django import forms
from django.core.exceptions import ValidationError

from .models import FootballPlayer


class AchievementForm(forms.Form):
    tournament = forms.CharField(min_length=3, max_length=25)
    achievement = forms.CharField(min_length=5, max_length=200)
    scored_goals = forms.IntegerField(min_value=0, max_value=200)
    appearances = forms.IntegerField(min_value=1)
    clean_sheets = forms.IntegerField(required=False)

    def clean_tournament(self):
        tournament_data = self.cleaned_data['tournament']
        if len(tournament_data.split(' ')) < 2 and tournament_data.capitalize():
            raise ValidationError("Please specify a Tournament name that consists of at least 2 words!")
        return tournament_data

    def clean_achievement(self):
        achievement_data = self.cleaned_data['achievement']
        if len(achievement_data.split(' ')) < 2:
            raise ValidationError("Please specify achievement that consists of at least 2 words!")
        return achievement_data

    def clean_appearances(self):
        appearances_data = self.cleaned_data['appearances']
        if appearances_data < 5:
            raise ValidationError("Minimum allowable quantity of the appearances in the season "
                                  "must be more then 5")
        return appearances_data

    def clean_scored_goals(self):
        scored_goals_data = self.cleaned_data['scored_goals']
        if scored_goals_data < 0:
            raise ValidationError("Allowed number of scored goals must be zero or more")
        return scored_goals_data

    def clean_clean_sheets(self):
        player = FootballPlayer.objects.filter(position="GK")
        clean_sheets_data = self.cleaned_data['clean_sheets']
        print(player)

        if player == "GK":

            raise ValidationError("Incorrect position is specified. "
                                  "\"Clean sheets\" field is allowed only for the \"GK\" position")
        return clean_sheets_data

    def clean(self):
        cleaned_data = super().clean()
        achievement = cleaned_data.get('achievement')
        appearances = cleaned_data.get('appearances')

        if not (appearances and achievement):
            self.add_error("appearances", "Note: both fields \"Appearances\" and \"Achievement\" are required")
