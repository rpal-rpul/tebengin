from django.db import models
from authentication.models import *

# Create your models here.
# class OrderStatus(models.TextChoices):
#     ACCEPTED = 'Accepted', _("Accepted")
#     REJECTED = 'Rejected', _("Rejected")
#     PENDING = 'Pending', _("Pending")
#     FINISHED = 'Finished', _("Finished")

    
# class Order(models.Model):
#     pickup_location = models.CharField(max_length=100)
#     destination_location = models.CharField(max_length=100)
#     order_date = models.DateTimeField()
#     pickup_date = models.DateTimeField()
#     distance = models.IntegerField(default=0)
#     fee = models.DecimalField(max_digits=30, decimal_places=2)
#     status = models.CharField(max_length=8, choices=OrderStatus.choices, default=OrderStatus.PENDING)
#     driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

