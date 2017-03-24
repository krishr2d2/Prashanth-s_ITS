from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^news/', views.news, name="news"),
    url(r'^contact/', views.contact, name="contact"),
    #url(r'^redirect/(?P<lat>[0-9]+\.[0-9]+)/(?P<lng>[0-9]+\.[0-9]+)/(?P<page>[a-z]+)', views.redirect, name="redirect"),

    # redirect/lat/lng/page
    url(r'redirect/(?P<lat>\d+\.\d+)/(?P<lng>\d+\.\d+)/', views.redirect, name="redirect"),
    
    url(r'^show_data/', views.show_data, name="show_data"),
    url(r'^insert/', views.insert.as_view(), name="insert"),

    url(r'current_data/(?P<lat>\d+\.\d+)/(?P<lng>\d+\.\d+)/(?P<temp>\d+)/(?P<humid>\d+)/(?P<carbon>\d+)/(?P<smo>\d+)', views.current_data, name="data"),

]