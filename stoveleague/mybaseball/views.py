from django.shortcuts import render
from mybaseball.models import Player

# Create your views here.

def index(request):
    return render(request, 'index.html')

def getplayerList(request):
    playerList = Player.objects.all().order_by("playerId")
    return render(request, "playerList.html", {"playerList":playerList})