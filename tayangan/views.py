from django.shortcuts import render

def show_tayangan(request):
    return render(request, "tayangan.html")

def show_result(request):
    return render(request, "pencarian_tayangan.html")

def show_film(request):
    return render(request, "film.html")

def show_episode(request):
    return render(request, "episode.html")

def show_series(request):
    return render(request, "series.html")