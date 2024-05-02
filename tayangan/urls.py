from django.urls import path
from tayangan.views import *

app_name = 'tayangan'

urlpatterns = [
    path('', show_tayangan, name='show_tayangan'),
    path('pencarian', show_result, name='show_result'),
    path('detail-film-1', show_film, name='show_film'),
    path('detail-series-2', show_series, name='show_series'),
    path('detail-episode-2-1', show_episode, name='show_episode'),
]