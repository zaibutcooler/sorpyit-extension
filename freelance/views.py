from django.shortcuts import render

# Create your views here.
def index(request):
	template="freelance/index.html"

	data={

	}

	return render(request,template,data)

def create(request):
	template="freelance/create.html"

	data={

	}

	return render(request,template,data)

def detail(request):
	template="freelance/detail.html"

	data={

	}

	return render(request,template,data)


def delete(request):
	template="freelance/elete.html"

	data={

	}

	return render(request,template,data)


def update(request):
	template="freelance/update.html"

	data={

	}

	return render(request,template,data)