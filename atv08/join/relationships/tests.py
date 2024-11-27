from django.test import TestCase
from .models import User, Profile, Author, Book, Student, Course

class ModelTestCase(TestCase):
    def setUp(self):
        # Configura dados para testes
        self.user = User.objects.create(name="John Doe", email="john@example.com")
        self.author = Author.objects.create(name="Jane Austen", birth_date="1775-12-16")
        self.course = Course.objects.create(name="Math", description="Math Course")
        self.student = Student.objects.create(name="Alice", enrollment_date="2023-01-01")
    
    def test_user_creation(self):
        """Testa a criação de um usuário"""
        self.assertEqual(self.user.name, "John Doe")
        self.assertEqual(self.user.email, "john@example.com")

    def test_author_creation(self):
        """Testa a criação de um autor"""
        self.assertEqual(self.author.name, "Jane Austen")
        self.assertEqual(self.author.birth_date, "1775-12-16") 


    def test_course_creation(self):
        """Testa a criação de um curso"""
        self.assertEqual(self.course.name, "Math")
        self.assertEqual(self.course.description, "Math Course")

    def test_student_relationship(self):
        """Testa o relacionamento N-N entre estudante e curso"""
        self.student.courses.add(self.course)
        self.assertIn(self.course, self.student.courses.all())
