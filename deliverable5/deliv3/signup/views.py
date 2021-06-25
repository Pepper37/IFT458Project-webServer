from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from .forms import Form

# Create your views here.

def index(request):
    return render(request, 'signup/index.html')

def signup(request):
    return render(request, 'signup/signup.html')


def test(request):
    return render(request, 'signup/test.html')


def form(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'signup/index.html')

    else:
        form = Form()
        context = {'form': form, }
    return render(request, 'signup/form.html', context)
