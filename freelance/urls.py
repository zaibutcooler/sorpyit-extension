from django.urls import path
from . import views

urlpatterns=[
	path('',views.index,name="findex"),
	path('create/',views.create,name="fcreate"),
	path('detail/<int:pk>',views.detail,name="fdetail"),
	path('update/<int:pk>',views.update,name="fupdate"),
	path('delete/<int:pk>',views.delete,name="fdelete"),



]