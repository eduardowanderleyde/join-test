from django.db import models

class Target(models.Model):
    """
    name: str
    latitude: float          
    longitude: float
    expiration_date: date
    """
    name = models.CharField(max_length=255)                    # Target name
    latitude = models.FloatField()                             # Latitude
    longitude = models.FloatField()                            # Longitude
    expiration_date = models.DateField()                       # Expiration Date

    def __str__(self):
        return self.name
