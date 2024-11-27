from django.db import models

# One-to-One Relationship
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

# One-to-Many Relationship
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()

# Many-to-Many Relationship
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Student(models.Model):
    name = models.CharField(max_length=100)
    enrollment_date = models.DateField()
    courses = models.ManyToManyField(Course)
