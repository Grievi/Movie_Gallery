from django.shortcuts import render
from django.contrib.auth import login,authenticate,logout

def user_login(request):
    message = 'Login to Proceed'

    return render(request, 'authentication/login.html', {"message": message})
