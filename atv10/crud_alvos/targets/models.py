from django.db import models

class Target(models.Model):
    identifier = models.CharField(max_length=100, unique=True)  # Identificador único
    name = models.CharField(max_length=255)                    # Nome do alvo
    latitude = models.FloatField()                             # Latitude
    longitude = models.FloatField()                            # Longitude
    expiration_date = models.DateField()                       # Data de Expiração

    def __str__(self):
        return self.name
