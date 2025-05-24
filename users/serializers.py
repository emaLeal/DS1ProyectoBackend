from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    '''User Serializer to return json'''
    # role = serializers.CharField(source='role.description')
    class Meta:
        model = User
        fields = ['name',
                  'last_name', 
                  'phone',
                  'cell_phone',
                  'email',
                  'document_id',
                  'gender',
                  'address',
                  'identification_type',
                  'birth_date',
                #   'role'
                  ]

