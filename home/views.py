from django.shortcuts import render

# Create your views here.
def index(request):
	template="home/index.html"

	data={

	}

	return render(request,template,data)


def about(request):
	template="home/about.html"

	data={

	}

	return render(request,template,data)

def login(request):
	template="home/login.html"

	data={

	}

	return render(request,template,data)

def logout(request):
	template="home/logout.html"

	data={

	}

	return render(request,template,data)

def register(request):
	template="home/register.html"

	data={

	}

	return render(request,template,data)

def profile(request):
	template="home/profile.html"

	data={

	}

	return render(request,template,data)

def projects(request):
	template="home/projects.html"

	data={

	}

	return render(request,template,data)