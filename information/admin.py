from django.contrib import admin
from .models import URL,URLType

# Register your models here.

class URLAdmin(admin.ModelAdmin):
	list_display = ('name','urltype','URL')
	fields  = ('name','URL','urltype','description')

	
admin.site.register(URLType)
admin.site.register(URL,URLAdmin)