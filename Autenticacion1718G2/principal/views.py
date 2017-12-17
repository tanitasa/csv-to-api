# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, get_object_or_404
from principal.models import Usuario
from django.template import RequestContext
from principal.serializers import UserSerializer, RoleSerializer
from rest_framework import generics
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User 
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view 
from rest_framework import viewsets, status


# Create your views here.

class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def getUsers(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UserSerializer(usuarios, many=True)
        return JSONResponse(serializer.data)


def getUser(request, usern):
    if request.method == 'GET':
        #dato = get_object_or_404(Usuario, username=usern)
        usuario = Usuario.objects.get(username=usern)
        serializer = UserSerializer(usuario)
        return JSONResponse(serializer.data)
    

def getRoleUser(request, usern):
    if request.method == 'GET':
        usuario = Usuario.objects.get(username=usern)
        rol = usuario.role
        r= 'True'
        m= 'Successfull'
        serializer = RoleSerializer({'result':r,'msg':m, 'role':rol})
        return JSONResponse(serializer.data)
    
    

def getUsersByRole(request, rol):
    if request.method == 'GET':
        usuarios = Usuario.objects.filter(role=rol)
        serializer = UserSerializer(usuarios, many=True)
        return JSONResponse(serializer.data)
    
class PostUser(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer

    