from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_form, name='payment_form'),
    path('success/<int:payment_id>/', views.payment_success, name='payment_success'),
]

