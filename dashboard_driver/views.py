from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from authentication.models import Driver
from dashboard_driver.forms import AddAvailableTimeForm
from dashboard_driver.models import DashboardDriver, OrderStatus


@csrf_exempt
def addAvailableTime(request):
    user = request.user

    if user.is_anonymous:
        return JsonResponse({"result": "Belum login"}, status=200)
    if request.method == 'POST':
        form = AddAvailableTimeForm(request.POST)
        driver = Driver.objects.get(user=user)

        if form.is_valid():
            form.save()
            driver.available_time.add(form.instance)
            response = {'result': 'berhasil'}
            return HttpResponse(response, status=200, content_type="application/json")
    return JsonResponse({"result": "not post method"}, status=200)


@csrf_exempt
def getDriverOrder(request):
    user = request.user
    if user.is_anonymous:
        return JsonResponse({"error": "Belum login"}, status=200)
    driver = Driver.objects.get(user=user)
    dashboard_driver = DashboardDriver.objects.get(driver=driver)

    value = {
        "accepted_order": list(dashboard_driver.order.filter(status=OrderStatus.ACCEPTED)),
        "rejected_order": list(dashboard_driver.order.filter(status=OrderStatus.REJECTED)),
        "pending_order": list(dashboard_driver.order.filter(status=OrderStatus.PENDING)),
        "history_order": list(dashboard_driver.order.filter(status=OrderStatus.FINISHED)),
    }

    return render(request, "dashboard_driver/index.html", value)
