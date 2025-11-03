from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_destination, name='add_destination'),
    path('edit/<int:id>/', views.edit_destination, name='edit_destination'),
    path('delete/<int:id>/', views.delete_destination, name='delete_destination'),
]