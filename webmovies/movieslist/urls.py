from django.urls import path
from . import views

app_movieslist="movieslist"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("<int:id>", views.movieView, name="movie-view"),
    path("newmovie/", views.newMovie, name="new-movie"),
    path('edit/<int:id>', views.editMovie, name="edit-movie"),
    path('delete/<int:id>', views.deleteMovie, name="delete-movie"),
]