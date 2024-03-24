from django.db import models
from core.models import User

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class MoviePerson(models.Model):
    class RoleType(models.TextChoices):
        ACTOR = 'actor', 'Actor'
        DIRECTOR = 'director', 'Director'
        COMPOSER = 'composer', 'Composer'

    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    photo = models.ImageField(
        upload_to='gn_01/images/person/photos',
        blank=True, null=True
    )
    biography = models.TextField()
    role = models.CharField(
        max_length=25, 
        choices=RoleType.choices,
        blank=True, null=True
    )


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.ImageField(
        upload_to='gn_01/images/movies/posters/',
        blank=True, null=True
    )
    embed = models.TextField()
    rating = models.FloatField(null=True, blank=True)
    releas_date = models.DateField()
    duration = models.PositiveSmallIntegerField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    age_limit = models.PositiveSmallIntegerField()
    actors = models.ManyToManyField(MoviePerson, related_name='acted_in_movie')
    directors = models.ManyToManyField(MoviePerson, related_name='directed_movie')
    composers = models.ManyToManyField(MoviePerson, related_name='composed_movie')
    budget = models.PositiveIntegerField()


class MovieReview(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, related_name='reviews'
    )
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, 
        related_name='reviews'
    )
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    author_advice = models.BooleanField(default=True, null=True, blank=True)

