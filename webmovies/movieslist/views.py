from django.shortcuts import render, get_object_or_404, redirect
from .models import MoviesList
from .forms import MovieForm
from django.contrib import messages

# Create your views here.

def homepage(request):
    movies = MoviesList.objects.all
    return render(
        request=request,
        template_name = "movieslist.html",
        context={"movies": movies},
    )

def movieView(request, id):
    movie_list = get_object_or_404(MoviesList, pk=id)
    return render(request, 'movies.html', {'movie_list': movie_list})

def newMovie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            movie = form.save(commit=False)
            movie.rank = '1'
            movie.save()
            return redirect('/')

    else:
        form = MovieForm()
        return render(request, 'addmovie.html', {'form': form})
    

def editMovie(request, id):
    movie = get_object_or_404(MoviesList, pk=id)
    form = MovieForm(instance=movie)

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)

        if form.is_valid():
            movie.save()
            return redirect('/')
        else:
            return render(request, 'editmovie.html', {'form': form, 'movie': movie})

    else:
        return render(request, 'editmovie.html', {'form': form, 'movie': movie})
    

def deleteMovie(request, id):
    movie = get_object_or_404(MoviesList, pk=id)
    movie.delete()
    messages.info(request, 'The movie has been deleted')
    return redirect('/')