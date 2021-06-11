from django.conf.urls import url
from app import views

urlpatterns=[
	url(r'^$', views.index, name='index'),
	url(r'^dominio/', views.dominio, name='dominio'),
	url(r'^ip/', views.ip, name='ip'),
]