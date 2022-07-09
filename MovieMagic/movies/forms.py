from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'poster', 'director', 'long_disc', 'short_disc', 'release_date', 'genre']
