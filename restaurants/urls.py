# restaurants/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('restaurants/', views.RestaurantList.as_view(), name='restaurant_list'),
    path('restaurants/<int:pk>',
         views.RestaurantDetail.as_view(), name='restaurant_detail'),
    path('reviews/', views.ReviewList.as_view(), name='review_list'),
    path('reviews/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),
]
