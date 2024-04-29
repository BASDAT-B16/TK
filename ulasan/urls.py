from django.urls import path
from ulasan.views import show_ulasan

app_name = 'ulasan'

urlpatterns = [
    path('', show_ulasan, name='show_ulasan'),
]