from django.urls import re_path
from . import views

app_name = 'user'

urlpatterns = [
    re_path('^index/$', views.index, name='index'),
    re_path(r'^say/$', views.say),
    re_path(r'^sayhello/$', views.sayhello),
    re_path(r'^rev/$', views.rev),
]