from django.conf.urls import url
from mainApp import views

app_name = 'mainApp'
urlpatterns = [
    url(r'^$', views.Home.as_view(),name='events'),
    url(r'^addevent/$', views.AddEvent.as_view(),name='add'),
    url(r'^events/(?P<pk>\d)/$', views.DetailEvent.as_view(),name='detail'),
    url(r'^subscribe/$', views.subscription,name='subscribe'),
    url(r'^aboutus/$', views.Aboutus.as_view(),name="aboutus"),
]
