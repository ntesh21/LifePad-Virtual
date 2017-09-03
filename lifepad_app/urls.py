
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
     url(r'^lifepad_project/', views.'lifepad_project', name="lifepad_project"),
     ]
    