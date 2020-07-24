from django.contrib import admin
from mybaseball.models import Player

# Register your models here.

class PlayerAdmin(admin.ModelAdmin):
   list_display=("name","team","war")

admin.site.register(Player, PlayerAdmin) 
