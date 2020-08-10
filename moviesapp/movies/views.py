# -*- coding: utf-8 -*-

"""Movies views."""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse_lazy

from .models import Movie


@login_required
def home(request);
return render(request, 'home.html', {})

class MovieListView(ListView):
    """Show all movies."""
    model = Movie


class MovieDetailView(DetailView):
    """Show the requested movie."""
    model = Movie

class MovieCreateView(CreateView):
    """Create a new movie."""
    model = Movie

class MovieUpdateView(UpdateView):
    """Update the requested movie."""
    model = Movie

class MovieDeleteView(DeleteView):
    """Delete the requested movie."""
     model = Movie

