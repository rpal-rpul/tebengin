from django.test import TestCase
from dashboard_customer.models import *
from dashboard_driver.models import *
from django.contrib.auth.models import User
from datetime import datetime

# Create your tests here.
class testModel(TestCase):
  def setUp(self):
    driver = User.objects.create_user(username="driver1", password="pass1")
    customer = User.objects.create_user(username="customer1", password="pass1")
    review = Review.objects.create(message="msg", driver=driver, customer=customer)

  def test_review_models(self):
    review = Review.objects.get(pk=1)
    driver = User.objects.get(username="driver1")
    customer = User.objects.get(username="customer1")
    self.assertEqual(review.message, "msg")
    self.assertEqual(review.driver, driver)
    self.assertEqual(review.customer, customer)
