from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from movies.forms import MovieForm
from movies.models import Movie


def home(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})


def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie': movie})


def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        director = request.POST['director']
        release_date = request.POST['date']
        long_disc = request.POST['long_disc']
        short_disc = request.POST['short_disc']
        genre = request.POST['genre']
        poster = request.FILES['poster']

        movie = Movie(title=title, director=director, release_date=release_date, long_disc=long_disc,
                      short_disc=short_disc, genre=genre, poster=poster)
        movie.save()
        return redirect('/')
    return render(request, 'add.html')


def edit(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, movie_id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=movie_id)
        title = movie.title
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')