from django.test import TestCase
from django.contrib.auth.models import User
from authentication.models import Pengguna, Driver, Customer
# Create your tests here.

class ProfilePageTest(TestCase):
    def setUp(self):
        user1 = self.user = User.objects.create_user(username='driver', password='testTest123a')
        user1.save()
        user2 = self.user = User.objects.create_user(username='customer', password='testTest123a')
        user2.save()
        self.driver = Driver.objects.create(user=user1)
        self.customer = Customer.objects.create(user=user2)
        self.driver.save()
        self.customer.save()

    def test_profile_page_driver_success(self):
        self.client.login(username='driver', password='testTest123a')
        response = self.client.get('/profile/')
        self.client.logout()
        self.assertEqual(response.status_code, 200)

    def test_profile_page_driver_fail(self):
        self.client.login(username='driver', password='testTest123a')
        response = self.client.get('/profilee/')
        self.client.logout()
        self.assertEqual(response.status_code, 404)
        