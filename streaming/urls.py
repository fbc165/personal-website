from django.urls import path
from . import views

urlpatterns = [
    path('', views.streaming_list, name='streaming_list'),
    path('<str:filename>/', views.streaming_player, name='streaming_player'),
]