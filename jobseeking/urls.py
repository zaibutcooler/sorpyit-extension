from django.urls import path
from . import views


urlpatterns=[
	path("",views.index,name="jindex"),
	path("create/",views.create,name="jcreate"),
	path("update/",views.update,name="jupdate"),
	path("detail/",views.detail,name="jdetail"),
	path("delete/",views.delete,name="jdelete"),


]