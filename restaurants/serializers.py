from rest_framework import serializers
from .models import Restaurant, Review


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    restaurant = serializers.HyperlinkedRelatedField(
        view_name='restaurant_detail', read_only=True)

    restaurant_id = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all(), source='restaurant')

    restaurant_name = serializers.SlugRelatedField(
        queryset=Restaurant.objects.all(), slug_field='name', source='restaurant')

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Review
        fields = ('id', 'restaurant', 'restaurant_id', 'title',
                  'body', 'created', 'restaurant_name', 'owner')


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    reviews = ReviewSerializer(
        many=True,
        read_only=True
    )

    restaurant_url = serializers.ModelSerializer.serializer_url_field(
        view_name='restaurant_detail')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'cuisine', 'reviews',
                  'restaurant_url', 'owner',)
