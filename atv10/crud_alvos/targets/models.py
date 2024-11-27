from django.db import models

class Target(models.Model):
    identifier = models.CharField(max_length=100, unique=True)  # Unique identifier
    name = models.CharField(max_length=255)                    # Target name
    latitude = models.FloatField()                             # Latitude
    longitude = models.FloatField()                            # Longitude
    expiration_date = models.DateField()                       # Expiration Date

    def __str__(self):
        return self.name
