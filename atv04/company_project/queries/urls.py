from django.urls import path
from . import views

urlpatterns = [
    path('query-a/', views.query_a, name='query_a'),
    path('query-b/', views.query_b, name='query_b'),
    path('query-c/', views.query_c, name='query_c'),
]
