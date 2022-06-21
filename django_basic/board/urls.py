from django.urls import path, include
from board import views

urlpatterns = [
    path('', views.boardlist),
    path('first/', views.boardfirst),
]
