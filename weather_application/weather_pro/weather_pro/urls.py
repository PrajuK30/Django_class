# weather_pro/urls.py
from django.contrib import admin
from django.urls import path, include  # Make sure to include 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather_app.urls')),  # This links the app's URLs to the root of the project
]