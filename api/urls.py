from django.urls import path
from . import views

urlpatterns = [
    path('examples/', views.members, name='example-list'),  # Sin paréntesis
]