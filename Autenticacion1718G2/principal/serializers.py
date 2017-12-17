from django.forms import widgets
from rest_framework import serializers
from principal.models import Usuario

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('result','msg','username','name', 'surname', 'email', 'genre', 'autonomous_community', 'age', 'role')
        
        def create(self, validated_data):

            return Usuario.objects.create(**validated_data)
        
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('result','msg','role')
        
        def create(self, validated_data):

            return Usuario.objects.create(**validated_data)