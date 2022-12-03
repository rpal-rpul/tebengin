from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from dashboard_customer.models import Driver, Customer, Review
from django.contrib.auth.models import User
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.
@csrf_exempt
def add_review(request):
    print(request.POST)
    print(request.user.id)
    if request.method == 'POST':
        id_customer = request.POST["id_customer"]
        id_driver = request.POST["id_driver"]
        message = request.POST["isi"]

        customer = User.objects.get(pk=id_customer)
        driver = User.objects.get(pk=id_driver)
        customer_login = User.objects.get(pk=request.user.id)

        print("ini driver", driver)
        print("ini cust", customer_login)
        # Create object
        Review.objects.create(message=message, driver=driver, customer=customer_login)
        return HttpResponse({})
        

@csrf_exempt
def get_review(request):
    if request.method == 'GET':
        data = list(Review.objects.values())
        return JsonResponse(data, safe=False)