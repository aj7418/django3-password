from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def apples(request):
    return HttpResponse('macs are the best')

def password(request):
    thePassword = ''

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('specialChars'):
        characters.extend(list('!@#$%^&*()_+'))

    length = int(request.GET.get('lengthPW'))

    for x in range(length):
        thePassword+=random.choice(characters)

    return render(request, 'generator/password.html', {'password':thePassword})

def about(request):
    return render(request, 'generator/about.html')
