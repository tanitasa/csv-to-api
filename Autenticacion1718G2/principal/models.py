# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from numpy import unique


ROLES=(('ASISTENTE','asistente'),('PONENTE',"ponente"),('AMBOS','ambos'))
GENEROS=(('MASCULINO','masculino'),('FEMENINO',"femenino"))
COMUNIDADES=(('ANDALUCIA','Andalucia'),('ARAGON','Aragon'),('ASTURIAS','Asturias'),('CANTABRIA','Cantabria'),('CASTILLA LA MANCHA','Castilla la mancha'),('CASTILLA LEON','Castilla leon'),('EXTREMADURA','Extremadura'),('GALICIA','Galicia'),('LA RIOJA','La rioja'),('MADRID','Madrid'),('MURCIA','Murcia'),('NAVARRA','Navarra'),('PAIS VASCO','Pais vasco'),('VALENCIA','Valencia'),('BALEARES','Baleares'),('CANARIAS','Canarias'),('CEUTA','Ceuta'),('MELILLA','Melilla'))

class Usuario(models.Model):
    usuario = models.OneToOneField(User, primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    genre = models.CharField(max_length=20,choices=GENEROS, default='-----')
    role = models.CharField(max_length=10, choices=ROLES, default='ASISTENTE')
    age = models.PositiveIntegerField()
    autonomous_community = models.CharField(max_length=50,choices=COMUNIDADES, default='-----')
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    msg = 'Successfull'
    result = 'True'
    
    def __unicode__(self):
        return self.name
    

    
    
