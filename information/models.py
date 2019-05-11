from django.db import models
from django.utils import timezone

# Create your models here.

'''
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
'''
class URLType(models.Model):
	#contact= models.ForeignKey(URLType,on_delete = models.CASCADE)
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name

class URL(models.Model):
	name = models.CharField(max_length=20)
	URL = models.TextField()
	urltype= models.ForeignKey(URLType,on_delete = models.CASCADE)
	description = models.TextField()
	def __str__(self):
		return self.name
# Create your models here.
