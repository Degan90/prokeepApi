from rest_framework import generics  # <- import generics
from .models import Restaurant, Review  # <- don't forget your models
from .serializers import RestaurantSerializer, ReviewSerializer  # <- or serializers
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    # check if user is authenticated before letting them post
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # overwrite the underlying perform_create method to save the owner as the user making the request
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # check if user is authenticated before letting them post
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]
