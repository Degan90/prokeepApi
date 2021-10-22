from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    owner = models.ForeignKey(
        'users.User', related_name='restaurants', default=None , on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.CharField(max_length=100)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='reviews')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'users.User', related_name='reviews', default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
