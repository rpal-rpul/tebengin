from django.db import models
from django.contrib.auth.models import User
from polymorphic.models import PolymorphicModel


class Pengguna(PolymorphicModel):
    email = models.EmailField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=100)
    distance_from_campus = models.IntegerField(blank=True, null=True, default=0)
    destination = models.CharField(max_length=100, blank=True, null=True, default="")
    USERNAME_FIELD = 'username'
    # rating = models.IntegerField(blank=True, null=True)
    # rating ntar diambil dari class rating


class AvailableDateTime(models.Model):
    available_time_begin = models.DateTimeField()
    available_time_end = models.DateTimeField()


class Driver(Pengguna):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    available_time = models.ManyToManyField(AvailableDateTime, blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    fee_per_km = models.IntegerField(blank=True, null=True)
    license_plate = models.CharField(max_length=20, blank=True, null=True)
    images = models.ImageField(upload_to='images/driver/', default='images/default.png')
    # review = models.CharField(max_length=100, blank=True, null=True)
    # review ntar diambil dari class review


class Customer(Pengguna):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/customer/', default='images/default.png')
