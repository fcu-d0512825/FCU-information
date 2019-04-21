from django.shortcuts import render

# Create your views here.

def mainpage(request):
    return render(request, 'information/mainpage.html', {})
def enroll(request):
    return render(request, 'information/mainpage.html', {})
def academic(request):
    return render(request, 'information/mainpage.html', {})
def research(request):
    return render(request, 'information/mainpage.html', {})
def life(request):
    return render(request, 'information/mainpage.html', {})
def about(request):
    return render(request, 'information/mainpage.html', {})