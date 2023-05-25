from django.urls import path
from . import views


urlpatterns=[
	path("",views.index,name="root"),
	path("about/",views.about,name="about"),
	path("profile/",views.profile,name="profile"),
	path("login/",views.login,name="login"),
	path("logout/",views.logout,name="logout"),
	path("projects/",views.projects,name="projects"),


]