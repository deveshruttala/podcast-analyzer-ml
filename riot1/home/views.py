from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("this is about page")