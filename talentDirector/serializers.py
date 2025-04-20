from rest_framework import serializers
from .models import TalentDirector

class TalentDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TalentDirector
        fields = [
            'document_id',
            'description',
        ]