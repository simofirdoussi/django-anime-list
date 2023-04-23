from anime_series.views import anime_list, anime_individual
from django.urls import path


urlpatterns = [
    path("", anime_list, name="home"),
    path("anime/<int:id>/", anime_individual, name="anime-individual"),
]
