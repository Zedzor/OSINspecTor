from django.conf.urls import include, url
from django.urls.resolvers import URLPattern 
from users import views

urlpatterns=[
    url(r'^logout/$', views.logout_view, name= 'logout_view'),
    url(r'^signup/$', views.signup_view, name= 'signup_view')
]