from django.db import models
from authentication.models import Driver, Customer
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Review(models.Model):
    message = models.TextField()
    date = datetime.now()
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Driver", blank=True, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Customer", blank=True, null=True)