from django import forms
from django.core.exceptions import ValidationError


class AchievementForm(forms.Form):
    tournament = forms.CharField(min_length=3, max_length=15)
    achievement = forms.CharField(min_length=5, max_length=200)

    def clean_tournament(self):
        tournament_data = self.cleaned_data['tournament']
        if len(tournament_data.split(' ')) < 2:
            raise ValidationError("Please specify a Tournament name that consists of at least 2 words!")
        return tournament_data

    def clean_achievement(self):
        achievement_data = self.cleaned_data['achievement']
        if len(achievement_data.split(' ')) < 2:
            raise ValidationError("Please specify achievement that consists of at least 2 words!")
        return achievement_data

    def clean(self):
        cleaned_data = super().clean()
        tournament = cleaned_data.get('tournament')
        achievement = cleaned_data.get('achievement')

        if tournament == achievement:
            self.add_error("achievement", "Note: the specified Achievement value must not match the Tournament value")

