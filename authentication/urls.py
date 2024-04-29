from django.urls import path
from authentication.views import show_authentication

app_name = 'authentication'

urlpatterns = [
    path('', show_authentication, name='show_authentication'),
]