from django.db import models

class Position(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='employees')
    hire_date = models.DateField()

    def __str__(self):
        return self.name
