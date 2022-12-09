from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from dashboard_driver.views import getDriverOrder, addAvailableTime

class TestUrls(SimpleTestCase):

    def setUp(self):
        self.dashboard_driver_url = reverse('dashboard_driver:getDriverOrder')
        self.add_datetime_url = reverse('dashboard_driver:addAvailableTime')

    def test_dashboard_driver_url_resolves(self):
        self.assertEqual(resolve(self.dashboard_driver_url).func, getDriverOrder)

    def test_add_datetime_resolves(self):
        self.assertEqual(resolve(self.add_datetime_url).func, addAvailableTime)
