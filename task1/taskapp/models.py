from django.db import models


# Create your models here.
class WhyUs(models.Model):
    head = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pictures')
    disc = models.TextField()

    def __str__(self):
        return self.head

class Team(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pictures')
    disc = models.TextField()

    def __str__(self):
        return self.name
