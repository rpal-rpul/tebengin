from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from .models import Pengguna, Driver, Customer, AvailableDateTime

admin.site.register(AvailableDateTime)


class ModelAChildAdmin(PolymorphicChildModelAdmin):
    base_model = Pengguna


@admin.register(Driver)
class ProductAdmin(ModelAChildAdmin):
    base_model = Driver  # Explicitly set here!
    show_in_index = True  # makes child model admin visible in main admin site


@admin.register(Customer)
class ProductAdmin(ModelAChildAdmin):
    base_model = Customer  # Explicitly set here!
    show_in_index = True  # makes child model admin visible in main admin site


@admin.register(Pengguna)
class ProductAdmin(PolymorphicParentModelAdmin):
    base_model = Pengguna  # Optional, explicitly set here.
    child_models = (Driver, Customer)


