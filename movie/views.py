from django.shortcuts import render

def index(request):
    message='Hello world'
    return render(request, 'movies/index.html',{"message": message})
