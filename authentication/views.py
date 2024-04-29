from django.shortcuts import render

def show_authentication(request):
    return render(request, "authentication.html")