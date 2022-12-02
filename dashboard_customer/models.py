from django.db import models
from authentication.models import Driver, Customer

# Create your models here.
class Review(models.Model):
    message = models.TextField()
    date = models.DateTimeField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)