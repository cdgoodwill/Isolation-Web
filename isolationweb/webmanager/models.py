import uuid
from django.db import models


class Place(models.Model):
    id = models.UUIDField(null=False, default=uuid.uuid4, primary_key=True)
    house_name = models.CharField(max_length=256)
    zip_code = models.CharField(max_length=10)
    lat = models.DecimalField(max_digits=11, decimal_places=8)
    lng = models.DecimalField(max_digits=11, decimal_places=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.house_name}"


class User(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    email = models.EmailField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.email}"


class UserConnection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    connected_place = models.UUIDField(null=False)
