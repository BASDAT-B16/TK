from django.shortcuts import render

def show_tayangan(request):
    return render(request, "tayangan.html")