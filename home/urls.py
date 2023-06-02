from django.urls import path
from . import views


urlpatterns=[
	path("",views.index,name="root"),
	path("about/",views.about,name="about"),
	path("profile/",views.profile,name="profile"),
	path("role-asking/",views.asking,name="asking"),

	# path('successful/',views.successful,name="successful")

	path("create-clientprofile/",views.clientcreateprofile,name="clientcreateprofile"),
	path("create-seekerprofile/",views.seekercreateprofile,name="seekercreateprofile"),
	path("login/",views.login,name="login"),
	path("logout/",views.logout,name="logout"),
	path("register/",views.register,name="register"),

	path("past-accomplishment/",views.create_projects,name="create_projects"),


]