from rest_framework import serializers
from .models import Postulant

class PostulantSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='document_id.get_full_name', read_only=True)
    email = serializers.EmailField(source='document_id.email', read_only=True)

    class Meta:
        model = Postulant
        fields = ['document_id', 'gender', 'identification_type', 'full_name', 'email']