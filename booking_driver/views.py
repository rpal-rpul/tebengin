import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from authentication.models import *
from dashboard_driver.models import *
from booking_driver.forms import BookingForm
from datetime import datetime
from django.core import serializers
from django.forms.models import model_to_dict

# Create your views here.

@csrf_exempt
def bookingDriver(request):
    user = request.user
    if user.is_anonymous:
        return JsonResponse({"result": "Belum login"}, status=200)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        customer = Customer.objects.get(user=user)
        if form.is_valid():
            form.save()
            response = {'result': 'berhasil'}
            return HttpResponse(response, status=200, content_type="application/json")
        return JsonResponse({"result": "not post method"}, status=200)

@csrf_exempt
def create_order(request):
    customer = request.user # Customer sedang login
    if customer.is_anonymous:
        return JsonResponse({"result": "Belum login"}, status=200)
    if request.method == 'POST':
        requested_datetime = request.POST.get("request_date")
        id_driver = request.POST.get("id_driver")
        pickup_location = request.POST.get("pickup_location")
        destination = request.POST.get("destination")
        fee = request.POST.get("fee")
        distance = request.POST.get("distance")
        driver = Driver.objects.get(id=id_driver)
        customer_object = Customer.objects.get(user=customer)

        created_order = Order.objects.create(pickup_location = pickup_location, destination_location = destination, pickup_date = requested_datetime, fee = fee, distance = distance, driver = driver, customer = customer_object)
        serialized_data = model_to_dict(created_order)
        serialized = json.dumps(serialized_data)
        return JsonResponse(json.loads(serialized), safe = False)

@csrf_exempt
@login_required(login_url='/authentication/login/')
def show_all_driver(request):
    customer = request.user # Customer sedang login
    if customer.is_anonymous:
        return JsonResponse({"result": "Belum login"}, status=200)
    if request.method == 'GET':
        driver_available = Driver.objects.all()
        context = {"models": driver_available}
        serialized_data = serializers.serialize('json', driver_available)

        return render(request, 'booking_driver.html', context)
    return JsonResponse(json.loads(serialized_data), safe = False)

@csrf_exempt
def show_filtered_driver(request):
    customer = request.user # Customer sedang login
    if customer.is_anonymous:
        return JsonResponse({"result": "Belum login"}, status=200)
    if request.method == 'POST':
        requested_datetime = request.POST.get("request_date")
        print(requested_datetime)
        driver_available = Driver.objects.filter(available_time__available_time_begin__lt = requested_datetime, available_time__available_time_end__gt = requested_datetime)
        serialized_data = serializers.serialize('json', driver_available)

        return JsonResponse(json.loads(serialized_data), safe = False)