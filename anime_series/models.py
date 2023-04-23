from django.db import models


# Create your models here.
class AnimeSerie(models.Model):
    name= models.CharField(max_length=200)
    image= models.URLField()
    description= models.CharField(max_length=1000, null=True)
    # characers = models.ManyToManyField('anime_series.Character')

    def __str__(self):
        return self.name

class Character(models.Model):
    name= models.CharField(max_length=200)
    image= models.URLField()
    description = models.CharField(max_length=800)

    order= models.PositiveIntegerField()
    anime_id= models.ForeignKey(
        AnimeSerie,
        related_name= "Character",
        on_delete=models.CASCADE
    )

    class Meta:
        ordering= ["order"]