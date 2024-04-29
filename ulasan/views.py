from django.shortcuts import render

def show_ulasan(request):
    return render(request, "ulasan.html")