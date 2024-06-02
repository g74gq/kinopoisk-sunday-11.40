from django.shortcuts import render, redirect
from .models import *

def add_movie_review(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        MovieReview.objects.create(
            author = request.user,
            movie = Movie.objects.get(id=movie_id),
            text = request.POST.get('review_text'),
        )
        return redirect('movie_detail', movie_id=movie_id)

def home(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(request, 'gn_01/home.html', context)

def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'gn_01/list/movies_list.html', {
        'movies': movies
    })

def actors_list(request):
    actors = MoviePerson.objects.filter(role=MoviePerson.RoleType.ACTOR).order_by('-id')
    return render(request, 'gn_01/list/actors_list.html', {
        'persons': actors, 'title': 'актеры'
    })

def directors_list(request):
    directors = MoviePerson.objects.filter(role=MoviePerson.RoleType.DIRECTOR).order_by('-id')
    return render(request, 'gn_01/list/directors_list.html', {
        'persons': directors, 'title': 'режисёры'
    })

def generes_list(request):
    generes = Genre.objects.all()
    return render(request, 'gn_01/list/generes_list.html', {
        'generes': generes, 'title': 'жанры'
    })

def composers_list(request):
    composers = MoviePerson.objects.filter(role=MoviePerson.RoleType.COMPOSER)
    return render(request, 'gn_01/list/composers_list.html', {
        'composers': composers
    })

def movies_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'gn_01/detail/movie_detail.html', {
        'movie': movie,
        # 'review': MovieReview.objects.filter(movie_id=movie_id).order_by('-created_at')
    })

def actors_detail(request, actors_id):
    actor = Movie.objects.get(id=actors_id)
    movies = actor.acted_in_movie.all()
    return render(request, 'gn_01/detail/actor_detail.html', {
        'actor': actor,
        'movie': movies
    })

def directors_detail(request, director_id):
    director = Movie.objects.get(id=director_id)
    movies = director.directed_movie.all()
    return render(request, 'gn_01/detail/directors_detail.html', {
        'director': director,
        'movie': movies
    })

def generes_detail(request, generes_id):
    genere = Genre.objects.get(id=generes_id)
    movies = genere.movies.all()
    return render(request, 'gn_01/detail/generes_detail.html', {
        'genere': genere,
        'movie': movies
    })

def composers_detail(request, composers_id):
    composer = Movie.objects.get(id=composers_id)
    movies = composer.composed_movie.all()
    return render(request, 'gn_01/detail/composers_detail.html', {
        'composer': composer,
        'movie': movies
    })