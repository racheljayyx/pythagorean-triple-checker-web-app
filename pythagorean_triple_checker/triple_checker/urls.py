from django.urls import path
from . import views

urlpatterns = [
    path('triple_checker/', views.triple_checker, name='triple_checker'),
]