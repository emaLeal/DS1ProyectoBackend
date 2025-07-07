from rest_framework import serializers
from job_offer.models import JobOffer

class JobOfferSerializer(serializers.ModelSerializer):
    talent_director_name = serializers.ReadOnlyField(source='talent_director_document.name')
    class Meta:
        model = JobOffer
        fields = [
            'title', 'responsibilities', 'start_date', 'end_date',
            'education_level', 'job_type', 'rank', 'other_requirements',
            'salary', 'status', 'talent_director_document','talent_director_name'
        ]