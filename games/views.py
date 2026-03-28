from django.shortcuts import render, get_object_or_404
from .models import Game

# Create your views here.
def game_list(request):
    games = Game.objects.all()

    context = {'games': games}
    return render(request, "games/game_list.html", context)

def game_detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    screenshot = game.screenshots.all()
    context = {
        "game": game,
        "screenshots": screenshot
    }
    return render(request, "games/game_detail.html", context)