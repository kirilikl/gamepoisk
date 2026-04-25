from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Screenshot


# Create your views here.
def game_list(request):
    games = Game.objects.all()

    context = {'games': games}
    return render(request, "games/game_list.html", context)

def game_detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)

    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:
            comment = Comment.objects.create(
                game=game,
                author=request.user,
                content=comment_text,
            )
            request.user.comment_count += 1
            request.user.save()
            return redirect('game_detail', game_id=game.id)

    if request.method == 'POST' and 'add_to_library' in request.POST:
            return redirect('add_to_library', game_id=game.id)

    comments = game.comment_set.all()
    screenshots = game.screenshots.all()

    context = {
        'game': game,
        'comments': comments,
        'screenshots': screenshots,
    }
    return render(request, 'games/game_detail.html', context)

