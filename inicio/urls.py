
from django.urls import path
from . import views  # <-- Add this line

app_name = "inicio"
urlpatterns = [
    path('', views.index, name='index'),
]