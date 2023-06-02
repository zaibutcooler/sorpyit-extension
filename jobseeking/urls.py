from django.urls import path
from . import views


urlpatterns=[
	path("",views.index,name="jindex"),
	path("create/",views.create,name="jcreate"),
	path("update/<int:pk>",views.update,name="jupdate"),
	path("detail/<int:pk>",views.detail,name="jdetail"),
	path("delete/<int:pk>",views.delete,name="jdelete"),


]