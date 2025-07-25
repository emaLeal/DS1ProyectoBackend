from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    '''User Serializer to return json'''
    role_description = serializers.CharField(source='role.description', read_only=True)
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
                  'role',
                  'role_description',
                  'date_joined'
                  ]

class ChangePasswordSerializer(serializers.Serializer):
    document_id = serializers.CharField(required=True)
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)