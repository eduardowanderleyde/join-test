from django.contrib import admin
from .models import User, Profile, Author, Book, Course, Student

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Course)
admin.site.register(Student)
