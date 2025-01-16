
from django.contrib import admin
from .models import City

# Register your models here.
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the city name in the admin interface
    search_fields = ('name',)  # Add a search box to find cities easily