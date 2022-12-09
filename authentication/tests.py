from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.contrib.auth.models import User
from authentication.models import Pengguna, Driver, Customer
# Create your tests here.

class AuthenticationTest(TestCase):
    def setUp(self):
        user1 = self.user = User.objects.create_user(username='driver', password='testTest123a')
        user1.save()
        user2 = self.user = User.objects.create_user(username='customer', password='testTest123b')
        user2.save()
        self.driver = Driver.objects.create(user=user1)
        self.driver.save()
        self.customer = Customer.objects.create(user=user2)
        self.customer.save()

    def test_authentication_driver_success(self):
        self.client.login(username='driver', password='testTest123a')
        response = self.client.get('')
        self.client.logout()
        self.assertEqual(response.status_code, 200)
        
    def test_authentication_customer_fail(self):
        self.client.login(username='customer', password='testTest123b')
        response = self.client.get('')
        self.client.logout()
        self.assertEqual(response.status_code, 200)