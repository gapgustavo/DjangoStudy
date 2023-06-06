from django import forms
from .models import MoviesList

class MovieForm(forms.ModelForm):

    class Meta:
        model = MoviesList
        fields = ('name', 'resume')