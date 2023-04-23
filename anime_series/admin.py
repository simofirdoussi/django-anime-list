from django.contrib import admin
from .models import AnimeSerie, Character

# Register your models here.
@admin.register(AnimeSerie)
class AnimeSerieAdmin(admin.ModelAdmin):
    list_display= (
        "name",
        "image",
        "description",
    )

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display= (
        "name",
        "image",
        "description",
    )