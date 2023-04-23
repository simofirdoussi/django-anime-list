from django.shortcuts import render
from anime_series.models import AnimeSerie, Character
from django.contrib.auth.decorators import login_required

# Create your views here.
def anime_list(request):
    animeseries= AnimeSerie.objects.all()
    context= {
        "animeseries": animeseries,
    }
    return render(request,"anime_series/anime.html", context)

def anime_individual(request, id):

    anime = AnimeSerie.objects.filter(id=id).first()
    characters = Character.objects.filter(anime_id=anime)

    context = {
        'anime': anime,
        'characters': characters
    }

    return render(request,"anime_series/individual.html", context)
