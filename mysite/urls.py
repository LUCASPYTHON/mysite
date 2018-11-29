"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from mysite.views import here,math,welcome,register
from livebroadcast.views import travel ,list_livebroadcasts,comment,login,index,logout

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^here/$',here),
    url(r'^math/$',math),
    url(r'^travel/(\d{1,5})/$',travel),
    url(r'^welcome/$',welcome),
    url(r'^livebroadcasts_list/$', list_livebroadcasts),
    url(r'^comment/(\d{1,5})/$', comment),
    url(r'^accounts/login/$',login),
    url(r'^index/$',index),
    url(r'^accounts/logout/$',logout),
    url(r'^accounts/register/$',register),

]
