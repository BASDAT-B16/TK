from django.urls import path
from trailer.views import show_trailer

app_name = 'trailer'

urlpatterns = [
    path('', show_trailer, name='show_trailer'),
]