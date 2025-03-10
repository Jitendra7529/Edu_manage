from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # Teacher URLs
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/create/', views.teacher_create, name='teacher_create'),
    path('teachers/update/<int:id>/', views.teacher_update, name='teacher_update'),
    path('teachers/delete/<int:id>/', views.teacher_delete, name='teacher_delete'),
    
    # Student URLs
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/update/<int:id>/', views.student_update, name='student_update'),
    path('students/delete/<int:id>/', views.student_delete, name='student_delete'),
    
    # Subject URLs
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/create/', views.subject_create, name='subject_create'),
    path('subjects/update/<int:id>/', views.subject_update, name='subject_update'),
    path('subjects/delete/<int:id>/', views.subject_delete, name='subject_delete'),
]