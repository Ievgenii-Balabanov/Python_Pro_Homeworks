from django.contrib import admin
from .models import FootballPlayer


class FootballPlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'club', 'transfer_fee', 'achievements')


admin.site.register(FootballPlayer, FootballPlayerAdmin)

# Register your models here.
