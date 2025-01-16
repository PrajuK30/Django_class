# weather_app/forms.py
from django import forms
from .models import City

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']  # Only take the 'name' field from the model (for city name)