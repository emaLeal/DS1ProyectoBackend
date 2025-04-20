from rest_framework import serializers
from job_offer.models import JobOffer

class JobOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        fields = [
            'title', 'responsibilities', 'start_date', 'end_date',
            'education_level', 'job_type', 'rank', 'other_requirements',
            'salary', 'status', 'talent_director_document'
        ]