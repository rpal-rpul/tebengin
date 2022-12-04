from django.db import models
from authentication.models import Driver, Customer
from dashboard_driver.models import Order, OrderStatus
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Review(models.Model):
    message = models.TextField()
    date = datetime.now()
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Driver", blank=True, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Customer", blank=True, null=True)

class DashboardCustomer(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    order = models.ManyToManyField(Order, blank=True)