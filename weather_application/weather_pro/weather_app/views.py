import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    api_key = '96e1f766b84245b2c4fdc3c473204dd1'  # Replace with your actual API key
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + api_key

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            # Save the city only if it's not already in the database (avoiding duplicates)
            city_name = form.cleaned_data['name'].lower()
            if not City.objects.filter(name__iexact=city_name).exists():
                form.save()
            else:
                print(f"City {form.cleaned_data['name']} already exists.")
        else:
            print(f"Form errors: {form.errors}")

    # Get all distinct cities (no duplicates)
    cities = City.objects.all().distinct()

    weather_data = []
    for city in cities:
        try:
            # Fetch weather data from the API
            response = requests.get(url.format(city.name)).json()
            if response.get('cod') == 200:  # Check if the response was successful
                weather = {
                    'city': city.name,
                    'temperature': response['main']['temp'],
                    'description': response['weather'][0]['description'],
                    'icon': response['weather'][0]['icon'],
                }
                weather_data.append(weather)
            else:
                print(f"Error fetching data for city {city.name}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for city {city.name}: {e}")
            weather_data.append({'city': city.name, 'error': 'Error fetching data'})

    context = {
        'weather_data': weather_data,
        'form': CityForm(),
    }

    return render(request, 'weather_app/index.html', context)