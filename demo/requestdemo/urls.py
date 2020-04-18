from django.urls import re_path
from . import views



urlpatterns = [
    re_path(r'^qs/$', views.qs),
    re_path(r'^weather/([a-z]+)/(\d{4})/$', views.weather),
    re_path(r'^form/$', views.get_body),
    re_path(r'^json/$', views.get_body_json),
    re_path(r'^response/$', views.responsefunc),
    re_path(r'^jsonfunc/$', views.jsonFunc),

]