from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def index(request):
	template="freelance/index.html"

	
	
	data={

	}

	return render(request,template,data)



def create(request):
	template="freelance/create.html"

	if request.method=="POST":
		title=request.POST['title']
		description=request.POST['description']		
		amount=request.POST['amount']		
		requirements=request.POST['requirements']		
		currency=request.POST['currency']		
		deadline=request.POST['deadline']		
		deadline_type=request.POST['deadline_type']		
		uploader=request.user

		offer=FreelanceOffer(uploader=uploader,title=title,description=description,amount=amount,requirements=requirements,currency=currency,deadline=deadline,deadline_type=deadline_type)

		if offer:
			offer.save()
			messages.success("Successfully Created")

		else:
			messages.success("Error")
	data={

	}

	return render(request,template,data)

def detail(request,pk):
	template="freelance/detail.html"

	offer=FreelanceOffer.objects.get(id=pk)

	data={
		"offer":offer
	}

	return render(request,template,data)


def delete(request,pk):
	template="freelance/elete.html"

	if request.method=="POST":
		offer=FreelanceOffer.objects.get(id=pk)
		if request.user==uploader:
			offer.delete()
	data={

	}

	return render(request,template,data)


def update(request,pk):
	template="freelance/update.html"

	data={

	}

	return render(request,template,data)