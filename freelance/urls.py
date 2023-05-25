from django.urls import path
from . import views

urlpatterns=[
	path('',views.index,name="findex"),
	path('create/',views.create,name="fcreate"),
	path('detail/',views.detail,name="fdetail"),
	path('update/',views.update,name="fupdate"),
	path('delete/',views.delete,name="fdelete"),



]