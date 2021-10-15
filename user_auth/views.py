from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm 

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
    messages.success(request, ("You have logged out"))
    return redirect('home')

def user_signup(request):
    message='Create an account here!'
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user= authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("Account created successfully"))

            return redirect('home')
            
    else:
        form=UserCreationForm()
    return render(request, 'authentication/signup.html', {"message": message,"form": form})