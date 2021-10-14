from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

def user_login(request):
    message = 'Login to Proceed'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,f"Welcome {username} to Movie Gallore!")
            return redirect('home')

        else:
            messages.success(request,"Oops Somethinge went wrong, please Login!")

            return render(request, 'authentication/login.html')
    else:
        return render(request, 'authentication/login.html', {"message": message})

    
def user_logout(request):

    logout(request)
    messages.success(request, "You have logged out")
    return redirect('home')