from django import forms
from authentication.models import Driver,Customer
import os
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'email', 'destination', 'distance_from_campus','images')
    
    def save(self, commit=True):
        old_image = Customer.objects.get(user=self.instance.user)
        new_image = self.cleaned_data['images']

        if new_image == old_image.images and old_image.images != '': # case kalau sebelumnya profpic, dan sekarang tidak ada profpic (default)
            os.remove(os.path.join(os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__))), 'media', str(old_image.images)))
            self.cleaned_data['images'] = None
            
        elif new_image != old_image.images and old_image.images != '': #case kalau sebelumnya ada gambar, dan sekarang diubah
            os.remove(os.path.join(os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__))), 'media', str(old_image.images)))
            
        # case kalau sebelumnya default, dan sekarang ada profpic
        customer = super(CustomerForm, self).save(commit=False)
        
        customer.images = self.cleaned_data['images']
        if commit:
            customer.save()
        return customer

    
class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('name', 'email', 'destination', 'distance_from_campus', 'phone_number', 'fee_per_km', 'license_plate','images')
        
    def save(self, commit=True):
        old_image = Driver.objects.get(user=self.instance.user)
        new_image = self.cleaned_data['images']

        if new_image == old_image.images and old_image.images != '': # case kalau sebelumnya profpic, dan sekarang tidak ada profpic (default)
            os.remove(os.path.join(os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__))), 'media', str(old_image.images)))
            self.cleaned_data['images'] = None
            
        elif new_image != old_image.images and old_image.images != '': #case kalau sebelumnya ada gambar, dan sekarang diubah
            os.remove(os.path.join(os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__))), 'media', str(old_image.images)))
        
        # case kalau sebelumnya default, dan sekarang ada profpic
        driver = super(DriverForm, self).save(commit=False)

        driver.images = self.cleaned_data['images']
        if commit:
            driver.save()
        return driver