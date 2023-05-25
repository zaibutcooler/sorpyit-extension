from django.shortcuts import render

# Create your views here.
def index(request):
	template="jobseeking/index.html"

	data={

	}

	return render(request,template,data)

def create(request):
	template="jobseeking/create.html"

	data={

	}

	return render(request,template,data)

def detail(request):
	template="jobseeking/detail.html"

	data={

	}

	return render(request,template,data)


def delete(request):
	template="jobseeking/delete.html"

	data={

	}

	return render(request,template,data)


def update(request):
	template="jobseeking/update.html"

	data={

	}

	return render(request,template,data)