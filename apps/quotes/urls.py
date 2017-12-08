from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add$', views.add, name="add"),
    url(r'^join/(?P<id>\d+)$', views.join, name="join"),
    url(r'^view/(?P<id>\d+)$', views.view, name="view"),
    url(r'^remove/(?P<id>\d+)$', views.remove, name="remove"),
]