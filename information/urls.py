from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
	path('enroll', views.enroll, name='enroll'),
	path('academic', views.academic, name='academic'),
	path('research', views.research, name='research'),
	path('life', views.life, name='life'),
	path('about', views.about, name='about'),
]