from django.shortcuts import render
from .models import Game

# Create your views here.
def game_list(request):
    games = Game.objects.all()

    context = {'games': games}
    print(context)
    return render(request, "games/game_list.html", context)