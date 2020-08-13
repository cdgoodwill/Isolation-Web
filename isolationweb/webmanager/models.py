import uuid
from django.db import models


# Places define physical entities. In the Isolation Web, they generally represent
# homes. Their residents are modeled as people, where people are abstractions of
# humans, in order to avoid privacy concerns.
#
# When people move between places, this creates connections. The connections are
# modeled between places.
#
# Covid statuses are set on people. They can be propagated up to places and spread
# visually throughout the isolation web to show risk and spread.
class Place(models.Model):
    id = models.UUIDField(null=False, default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=256)
    zip_code = models.CharField(max_length=10)
    lat = models.DecimalField(max_digits=11, decimal_places=8)
    lng = models.DecimalField(max_digits=11, decimal_places=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class ConnectedPlace(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    connected_place = models.UUIDField(null=False)


class Person(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


# Users represent users of the system. They each own a Place, which they
# are able to edit.
class User(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    email = models.CharField(unique=True, max_length=1024)

    def __str__(self):
        return f"{self.email}"
