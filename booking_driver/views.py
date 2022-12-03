from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from authentication.models import *
from dashboard_driver.models import *
from booking_driver.forms import BookingForm

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

