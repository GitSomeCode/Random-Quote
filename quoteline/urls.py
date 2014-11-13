from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from quoteline import views

urlpatterns = patterns('',
  url(r'^index/$', views.GreetingView.as_view(), name="greeting"),  
  url(r'^showquote/$', views.ShowQuote.as_view(), name="display"),
)