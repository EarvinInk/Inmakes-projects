from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='poster')
    short_disc = models.CharField(max_length=250)
    long_disc = models.TextField()
    director = models.CharField(max_length=50)
    release_date = models.IntegerField()
    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.title
