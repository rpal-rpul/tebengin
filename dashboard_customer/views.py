from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from dashboard_customer.models import Driver, Customer, Review
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
@csrf_exempt
def add_review(request):
    if request.method == 'POST':
        username_customer = request.POST.get("username_customer")
        username_driver = request.POST.get("username_driver")
        message = request.POST.get("isi")
        customer = Customer.objects.get(user=username_customer)
        driver = Driver.objects.get(user=username_driver)

        # Create object
        return JsonResponse(Review.objects.create(message, datetime.now(), driver, customer))
        

@csrf_exempt
def get_review(request):
    if request.method == 'GET':
        print(Review.objects.all())
        return Review.objects.all()