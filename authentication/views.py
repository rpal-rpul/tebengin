from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from authentication.forms import ChoiceRoleForm, CustomerRoleForm, DriverRoleForm
from django.contrib.auth import authenticate, login, logout
from dashboard_driver.models import DashboardDriver
from .models import Driver, Customer
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    formulir = ChoiceRoleForm()
    argument = {
        'form': formulir,
        'formrole': True,
        'roleDriver': False,
        'roleCustomer': False
    }
    return render(request, 'authentication/registerRole.html', argument)

@csrf_exempt
def registerPenggunaRole(request, message="", role=None):
    try:
        Role = str(request.POST['Role'])
    except:
        Role = role

    roleDriver = False
    roleCustomer = False
    formulir = None
    if (Role == "Driver"):
        formulir = DriverRoleForm(data=request.POST)
        roleDriver = True
    elif (Role == "Customer"):
        formulir = CustomerRoleForm(data=request.POST)
        roleCustomer = True

    argument = {
        'form': formulir,
        'Role': Role,
        'roleDriver': roleDriver,
        'roleCustomer': roleCustomer,
        'message': message
    }
    return render(request, 'authentication/register.html', argument)

@csrf_exempt
def register_driver(request):
    form = DriverRoleForm(request.POST)
    if form.is_valid():
        form.save()

        if request.method == "POST":
            username = request.POST['username']
            email = request.POST['email']
            # images = request.FILES['images']

            user = User.objects.get(username=username)
            driver = Driver.objects.create(user=user, email=email)
            DashboardDriver.objects.create(driver=driver)
            return redirect('/authentication/login/')
    return render(request, 'authentication/register.html', {'form': form})

@csrf_exempt
def register_customer(request):
    form = CustomerRoleForm(request.POST)
    if form.is_valid():
        form.save()

        if request.method == "POST":
            username = request.POST['username']
            email = request.POST['email']
            # images = request.FILES['images']

            user = User.objects.get(username=username)
            Customer.objects.create(user=user, email=email)

            return redirect('/authentication/login/')
    return render(request, 'authentication/register.html', {'form': form})

@csrf_exempt
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'authentication/login.html', {'message': 'Wrong username or password'})
    return render(request, 'authentication/login.html')


def logout_user(request):
    logout(request)
    return redirect('/')
