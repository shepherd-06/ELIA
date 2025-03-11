from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # A basic example
    # Add more URL patterns here for other views
]