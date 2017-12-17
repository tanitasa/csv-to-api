"""Autenticacion1718G2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from principal import views
from rest_framework.urlpatterns import format_suffix_patterns
from principal.views import PostUser


post_list = views.PostUser.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^getUsers/$', views.getUsers),
    url(r'^getUser/(.+)/$', views.getUser),
    url(r'^getRoleUser/(.+)/$', views.getRoleUser),
    url(r'^getUsersByRole/(.+)/$', views.getUsersByRole),
    url(r'^postUser/$', post_list, name='post_list'), 

    
    #token
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),


]
