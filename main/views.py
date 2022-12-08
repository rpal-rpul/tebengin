from django.shortcuts import render

def home(request):
    profile = request.user
    context = {
        'user': profile,
    }
    return render(request, 'home.html', context)

def template_example(request):
    return render(request, 'template_example.html', {})