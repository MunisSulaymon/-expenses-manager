from django.urls import path
from . import views

urlpatterns = [
    path('', views.outcome_list, name='outcome_list'),
    path('add/', views.outcome_add, name='outcome_add'),
    path('edit/<int:pk>/', views.outcome_edit, name='outcome_edit'),
    path('delete/<int:pk>/', views.outcome_delete, name='outcome_delete'),
]