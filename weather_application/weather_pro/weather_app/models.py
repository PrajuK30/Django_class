from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Ensure city names are unique
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name
