# weather_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This links the root URL of this app to the index view
]