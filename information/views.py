from django.shortcuts import redirect, render
from .models import URL,URLType

# Create your views here.

def mainpage(request):
	url = URL.objects.all()
	urlType = URLType.objects.all()
	return render(request, 'information/mainpage.html', {'url': url,'urlType':urlType})