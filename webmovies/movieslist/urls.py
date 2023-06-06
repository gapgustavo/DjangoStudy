from django.urls import path
from . import views

app_movieslist="movieslist"

urlpatterns = [
    path("", views.homepage, name="homepage")
]