from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    '''User Serializer to return json'''
    class Meta:
        model = User
        fields = ['name', 'last_name', 'phone','email','document_id', 'password','address']