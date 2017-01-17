# add url for send_email
from django.conf.urls import url
from . import views

urlpatterns = [url(r'^contact/$', views.send_email, name='send_email')]
