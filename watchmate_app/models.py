from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    rating = models.FloatField()
    runtime = models.IntegerField()
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    actors = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    trailer = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title