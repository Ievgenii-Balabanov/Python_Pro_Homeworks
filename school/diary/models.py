from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class FootballPlayer(models.Model):
    name = models.CharField(max_length=20, default=None)
    position = models.CharField(max_length=5, default=None)
    transfer_fee = models.IntegerField(default=0)
    club = models.CharField(max_length=2, default=None)
