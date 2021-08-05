from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('procesar/' , views.procesar),
    path('reseteo/', views.reseteo),
]
