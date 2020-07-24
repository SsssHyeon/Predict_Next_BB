from django.db import models
from datetime import datetime

# Create your models here.
class Player(models.Model):
    playerId=models.AutoField(primary_key=True)
    name=models.CharField(max_length=256)
    team=models.CharField(max_length=256)
    salary=models.CharField(max_length=1024)
    war=models.CharField(max_length=256)

    def hit_up(self):
        self.hit += 1
    def down_up(self):
        self.down += 1 