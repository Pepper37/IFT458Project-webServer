from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'signup/index.html')

def signup(request):
    return render(request, 'signup/signup.html')


def test(request):
    return render(request, 'signup/test.html')
