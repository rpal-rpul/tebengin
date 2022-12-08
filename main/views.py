from django.shortcuts import render

def home(request):
    profile = request.user
    context = {
        'user': profile,
    }
    return render(request, 'home.html', context)