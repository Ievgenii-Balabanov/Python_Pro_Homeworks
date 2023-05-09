from django.db import models
import views

# Create your models here.


class FootballPlayer(models.Model):
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=5)
    transfer_fee = views.add_fee()


