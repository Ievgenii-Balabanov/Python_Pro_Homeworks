from django.contrib import admin
from .models import FootballPlayer, Achievement


class FootballPlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'club', 'transfer_fee',)


class AchievementAdmin(admin.ModelAdmin):
    list_display = ('tournament', 'achievement',)


admin.site.register(FootballPlayer, FootballPlayerAdmin)
admin.site.register(Achievement, AchievementAdmin)
