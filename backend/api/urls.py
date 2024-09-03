from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_home),
    path('api_home2/', views.api_home2),
    path('api_home3/', views.api_home3),
    path('api_home4/', views.api_home4),
    path('api_home5/', views.api_home5),
]