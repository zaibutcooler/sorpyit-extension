from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout as auth_logout
from .models import *
from django.contrib import messages


def index(request):
    template = "home/index.html"
    data = {}
    return render(request, template, data)


def about(request):
    template = "home/about.html"
    data = {}
    return render(request, template, data)


def login(request):
    template = "home/login.html"

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('root')
        else:
            error_message = "Invalid username or password"
            return render(request, template, {"error_message": error_message})

    data = {}
    return render(request, template, data)


def logout(request):
    template = "home/logout.html"

    if request.method == "POST":
        auth_logout(request)
        return redirect('root')

    data = {}
    return render(request, template, data)


def register(request):
    template = "home/register.html"

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createprofile')
        else:
            return redirect('register')

    data = {}
    return render(request, template, data)


def profile(request):
    template = "home/profile.html"
    data = {}
    return render(request, template, data)


def asking(request):
    template = "home/askingcf.html"
    data = {}
    return render(request, template, data)


def clientcreateprofile(request):
    template = "home/client_create_profile.html"
    user = request.user

    if ClientProfile.objects.filter(user=user).exists():
        return redirect('root')

    if request.method == 'POST':
        name = request.POST.get('name')
        profile_picture = request.FILES.get('profile_picture')
        organization = request.POST.get('organization')
        organization_link = request.POST.get('organization_link')
        bio = request.POST.get('bio')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')

        profile = ClientProfile.objects.create(
            name=name,
            profile_picture=profile_picture,
            organization=organization,
            organization_link=organization_link,
            bio=bio,
            email=email,
            phonenumber=phonenumber,
            user=user.id  # Pass the user ID instead of the user object
        )

        return redirect('home')

    data = {}
    return render(request, template, data)


def seekercreateprofile(request):
    template = "home/seeker_create_profile.html"
    user=request.user

    if NormalProfile.objects.filter(user=user).exists():
        return redirect('root')

    if request.method == 'POST':
        name = request.POST.get('name')
        profile_picture = request.FILES.get('profile_picture')
        socialmedia = request.POST.get('socialmedia')
        bio = request.POST.get('bio')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        highschool = request.POST.get('highschool')
        college = request.POST.get('college')

        profile = NormalProfile.objects.create(
            name=name,
            profile_picture=profile_picture,
            socialmedia=socialmedia,
            bio=bio,
            email=email,
            phonenumber=phonenumber,
            highshcool=highschool,
            collage=college,
            user=request.user
        )

        return redirect('login')

    data = {}
    return render(request, template, data)


def create_projects(request):
    template = "home/create_projects.html"

    if request.method=="POST":
        title=request.POST['title']
        description=request.POST['description']
        time=request.POST['time']
        link=request.POST['link']

        project = Project(title=title, description=description, time=time, link=link)

        if project:
            project.save()
            messages.success(request, "Added to your profile")
        else:
            messages.error(request, "Invalid project data")

    data = {}
    return render(request, template, data)
