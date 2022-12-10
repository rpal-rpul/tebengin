from django.shortcuts import render, redirect, HttpResponseRedirect
from authentication.models import Pengguna,Driver,Customer
from profilepage.forms import CustomerForm, DriverForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages 

@login_required(login_url='/authentication/login')
def profile(request):
    
    profile, is_driver, is_customer = get_profile(request)
    profile.is_authenticated = True
    context = {
        'user': request.user,
        'profile': profile,
        'isdriver': is_driver,
        'iscustomer': is_customer,
    }
    return render(request, 'profilepage/profilepage.html', context)
    
@login_required(login_url='/authentication/login')
def update_data(request):
    profile, is_driver, is_customer = get_profile(request)
    
    if request.method == 'POST':
        if is_driver:
            form = DriverForm(request.POST,request.FILES, instance=profile.driver)
        else:
            form = CustomerForm(request.POST, request.FILES, instance=profile.customer)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your data was successfully updated!')
            return HttpResponseRedirect('/profile')
        
    if is_driver:
        form = DriverForm(instance=profile.driver)
    else:
        form = CustomerForm(instance=profile.customer)
    context = {
        'form': form,
        'profile': profile,
        'isdriver': is_driver,
        'iscustomer': is_customer,
    }
    return render(request, 'profilepage/edit_data.html', context)

@login_required(login_url='/authentication/login')
def change_password(request):
    profile, is_driver, is_customer = get_profile(request)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/profile')
        else:
            return render(request, 'profilepage/change_password.html', {
                'form': form,
                'profile': profile,
                'isdriver': is_driver,
                'iscustomer': is_customer,
            })
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
        'profile': profile,
        'isdriver': is_driver,
        'iscustomer': is_customer,
    }
    return render(request, 'profilepage/change_password.html', context)

    
def get_profile(request):
    current_user = request.user
    # get current user's profile from polymorphic model
    try:
        profile = Pengguna.objects.filter(driver__user=current_user)[0]
        isdriver,iscustomer = True,False
    except:
        profile = Pengguna.objects.filter(customer__user=current_user)[0]
        isdriver,iscustomer = False,True
    profile.is_authenticated = True
    
    return profile, isdriver, iscustomer