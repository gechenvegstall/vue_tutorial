from django.urls import path
from . import views

urlpatterns = [
    path('subjects/', views.show_subjects, name='show_subjects'),
    path('teachers/', views.show_teachers, name='show_teachers'),
]