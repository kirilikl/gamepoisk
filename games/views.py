from django.shortcuts import render

GAMES = [
    "SugarCrash",
    "Змейка",
    "Сапёр",
    "Смута",
    "World of Tanks",
    "Flight Simulator",
    "WarCraft",
    "Gardenscapes"
]

# Create your views here.
def game_list(request):
    query = request.GET.get("q")
    if query:
        filtered_games = [game for game in GAMES if query.lower() in game.lower()]
    else:
        filtered_games = GAMES

    context = {'games': filtered_games}
    return render(request, "games/game_list.html", context)