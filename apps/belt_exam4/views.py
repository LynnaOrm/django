from __future__ import unicode_literals
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import date

# Create your views here.
def index(request):
    return render(request,'belt_exam4/index.html')

def register(request):
    print request.POST
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully Registered!")
    return redirect('/quotes')


def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully Logged in!")
    today = date.today().strftime("%Y-%m-%d_%H:%M")
    return redirect('/quotes')

def logout(request):
    request.session.clear()
    return redirect('/')

