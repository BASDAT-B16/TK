from django.urls import path
from tayangan.views import show_tayangan

app_name = 'tayangan'

urlpatterns = [
    path('', show_tayangan, name='show_tayangan'),
]