from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^join/(?P<id>\d+)$', views.join, name='join'),
  url(r'^add$', views.add, name='add'),
  url(r'^new$', views.new, name='new'),
  url(r'^destination/(?P<id>\d+)$', views.dest, name='dest'),
]
