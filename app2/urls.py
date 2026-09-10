
from django.urls import path
from . import views  # <-- Add this line

app_name = "app2"

urlpatterns = [
    path('v1/', views.v1, name='v1'),
    path('v2/', views.v2, name='v2'),
]