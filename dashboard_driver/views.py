from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from authentication.models import Driver
from dashboard_driver.forms import AddAvailableTimeForm
from dashboard_driver.models import DashboardDriver, OrderStatus
from django.forms.models import model_to_dict


@csrf_exempt
@login_required(login_url='/authentication/login/')
def addAvailableTime(request):
    user = request.user

    if request.method == 'POST':
        form = AddAvailableTimeForm(request.POST)
        driver = Driver.objects.get(user=user)

        if form.is_valid():
            form.save()
            driver.available_time.add(form.instance)
            return JsonResponse(model_to_dict(form.instance), status=200, content_type="application/json")
        return JsonResponse({"failed": "Failed to save available time"}, status=405)
    return JsonResponse({"failed": "Not using POST method"}, status=405)


@csrf_exempt
@login_required(login_url='/authentication/login/')
def getDriverOrder(request):
    user = request.user
    if request.method == 'GET':
        driver = Driver.objects.get(user=user)
        dashboard_driver = DashboardDriver.objects.get(driver=driver)
        value = {
            "accepted_order": list(dashboard_driver.order.filter(status=OrderStatus.ACCEPTED)),
            "rejected_order": list(dashboard_driver.order.filter(status=OrderStatus.REJECTED)),
            "pending_order": list(dashboard_driver.order.filter(status=OrderStatus.PENDING)),
            "history_order": list(dashboard_driver.order.filter(status=OrderStatus.FINISHED)),
        }
        return render(request, "dashboard_driver/index.html", value)
    return JsonResponse({"failed": "Not using GET method"}, status=405)
