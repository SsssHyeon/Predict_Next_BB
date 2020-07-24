from django.shortcuts import render
from mybaseball.models import Player

# Create your views here.

def index(request):
    return render(request, 'index.html')

def playerList(request):
    playerList=Player.objects.all().order_by("-idx")
    return render(request, "playerList.html", {"playerListt":playerList})