from django.contrib import admin
from django.conf.urls import url
from me import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home),
    url(r'^about/$', views.about, name='about'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^connect/$', views.connect, name='connect'),
]
