from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),                    # Home / List students
    path('add/', views.add_student, name='add_student'),                 # Add student
    path('edit/<int:id>/', views.update_student, name='update_student'), # Edit student
    path('delete/<int:id>/', views.delete_student, name='delete_student'), # Delete student
    path('register/', views.register, name='register'),                  # Admin registration
]




