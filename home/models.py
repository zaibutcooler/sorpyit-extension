from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Portfolio(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	title=models.CharField(max_length=100)
	description=models.CharField(max_length=100)
	link=models.CharField(max_length=100)

	def __str__(self):
		return self.title

	
class NormalProfile(models.Model):
	name=models.CharField(max_length=100)
	profile_picture=models.ImageField(blank=True,null=True)
	socialmedia=models.CharField(max_length=300)
	bio=models.TextField(blank=True,null=True)
	email=models.EmailField()
	phonenumber=models.CharField(max_length=20,blank=True,null=True)
	highshcool=models.CharField(max_length=100,blank=True,null=True)
	collage=models.CharField(max_length=100,blank=True,null=True)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name

class ClientProfile(models.Model):
	name=models.CharField(max_length=100)
	profile_picture=models.ImageField(blank=True,null=True)
	organization=models.CharField(max_length=100,blank=True,null=True)
	organization_link=models.CharField(max_length=100,blank=True,null=True)
	bio=models.TextField(blank=True,null=True)
	email=models.EmailField()
	phonenumber=models.CharField(max_length=20,blank=True,null=True)
	user=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Project(models.Model):
	title=models.CharField(max_length=200)
	description=models.TextField()
	time=models.DateField()
	link=models.CharField(max_length=400)

	def __str__(self):
		return self.title
