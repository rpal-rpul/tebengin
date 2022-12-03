from django.shortcuts import redirect,render
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from authentication.forms import ChoiceRoleForm, CustomerRoleForm, DriverRoleForm
from django.contrib.auth import authenticate, login, logout
from .models import Driver, Customer
from django.views.decorators.csrf import csrf_exempt

def register(request):
    formulir = ChoiceRoleForm()
    argument = { 
        'form' : formulir,
        'formrole' : True,
        'roleDriver' : False,
        'roleCustomer' : False
    }
    return render(request, 'authentication/register.html', argument)

def registerPenggunaRole(request, message="", role=None):
    try:
        Role = str(request.POST['Role'])
    except:
        Role = role
        
    roleDriver = False
    roleCustomer = False
    formulir = None
    if(Role == "Driver"):
        formulir = DriverRoleForm(data = request.POST, files = request.FILES)
        roleDriver = True
    elif(Role == "Customer"):
        formulir = CustomerRoleForm(data = request.POST, files = request.FILES)
        roleCustomer = True

    argument = { 
        'form' : formulir,
        'Role' : Role,
        'roleDriver' : roleDriver,
        'roleCustomer' : roleCustomer,
        'message': message
    }
    return render(request, 'authentication/register.html', argument)

def register_driver(request):
    form = DriverRoleForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        
        if request.method == "POST":
            username = request.POST['username']
            email = request.POST['email']
            images = request.FILES['images']
            
            user = User.objects.get(username=username)
            Driver.objects.create(user=user, email=email, images=images)
            
            return redirect('/authentication/login/')

def register_customer(request):
    form = CustomerRoleForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        
        if request.method == "POST":
            username = request.POST['username']
            email = request.POST['email']
            images = request.FILES['images']
            
            user = User.objects.get(username=username)
            Customer.objects.create(user=user, email=email, images=images)
            
            return redirect('/authentication/login/')


@csrf_exempt
def sign_in(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # redirect ke home
            return redirect('/')

    return render(request, 'authentication/login.html')

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

