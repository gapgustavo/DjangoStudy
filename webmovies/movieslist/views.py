from django.shortcuts import render
from .models import MoviesList

# Create your views here.

def homepage(request):
    return render(
        request=request,
        template_name = "home.html",
        context={"movies": MoviesList.objects.all},
    )
