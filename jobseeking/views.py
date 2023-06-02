from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
	template="jobseeking/index.html"

	data={

	}

	return render(request,template,data)

def create(request):
	template="jobseeking/create.html"

	if request.method=="POST":
		title=request.POST['title']
		description=request.POST['description']
		country=request.POST['country']
		city=request.POST['city']
		salary=request.POST['salary']
		onsite=request.POST['onsite']
		requirements=request.POST['requirements']
		responsibilities=request.POST['responsibilities']
		email=request.POST['email']
		phonenumber=request.POST['phonenumber']
		uploader=request.user

		offer = JobOffer(title=title,description=description,country=country,city=city,salary=salary,onsite=onsite,requirements=requirements,responsibilities=request,email=email,phonenumber=phonenumber,uploader=uploader)
	
		if offer:
			offer.save()
			messages.success(request,"Successfully uploaded")
		else:
			messages.success(request,"Error")
	data={

	}

	return render(request,template,data)



def detail(request,pk):
	template="jobseeking/detail.html"
	offer=JobOffer.objects.get(id=pk)
	data={
		'offer':offer
	}

	return render(request,template,data)


def delete(request,pk):
	template="jobseeking/delete.html"

	if request.method=="POST":
		offer=JobOffer.objects.get(id=pk)
		if offer.uploader==request.user:
			offer.delete()
			redirect('root')
	data={

	}

	return render(request,template,data)


def update(request,pk):
	template="jobseeking/update.html"

	data={

	}

	return render(request,template,data)