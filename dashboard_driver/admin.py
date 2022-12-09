from django.contrib import admin

# Register your models here.
from dashboard_driver.models import DashboardDriver, Order

admin.site.register(DashboardDriver)
admin.site.register(Order)
