from rest_framework import viewsets, permissions
from moviesapp.movies.models import Movie
from .serializers import MovieSerializer

# Movie viewset

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = MovieSerializer