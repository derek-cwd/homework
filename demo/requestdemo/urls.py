from django.urls import re_path
from . import views



urlpatterns = [
    re_path(r'^qs/$', views.qs),
    re_path(r'^weather/([a-z]+)/(\d{4})/$', views.weather),

]