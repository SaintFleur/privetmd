from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from mdb import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dataset/',views.DatasetList.as_view()),
]

urlpatterns=format_suffix_patterns(urlpatterns)