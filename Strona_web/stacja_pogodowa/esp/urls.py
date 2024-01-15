from django.urls import path
from . import views

urlpatterns = [
    path('', views.esp, name='esp'),
]