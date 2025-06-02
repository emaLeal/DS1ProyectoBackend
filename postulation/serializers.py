from rest_framework import serializers
from .models import Postulation

class PostulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulation
        fields = [
            'applicant_document',
            'job_offer_id',
            'undergraduate_title',
            'postgraduate_title',
            'motivation',
            'resume',
            'phone',
            'application_date'
        ]
