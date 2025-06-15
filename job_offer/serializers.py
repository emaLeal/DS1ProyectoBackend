from rest_framework import serializers
from job_offer.models import JobOffer
from datetime import date

class JobOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        fields = [
            'title', 'responsibilities', 'start_date', 'end_date',
            'education_level', 'job_type', 'rank', 'other_requirements',
            'salary', 'status', 'talent_director_document'
        ]

    def validate(self, data):
        # Validar que la fecha de inicio no sea anterior a hoy
        if 'start_date' in data and data['start_date'] < date.today():
            raise serializers.ValidationError({
                "start_date": "La fecha de inicio no puede ser anterior a hoy"
            })

        # Validar que la fecha de fin sea posterior a la de inicio
        if 'start_date' in data and 'end_date' in data:
            if data['end_date'] < data['start_date']:
                raise serializers.ValidationError({
                    "end_date": "La fecha de fin debe ser posterior a la fecha de inicio"
                })

        # Validar que el salario sea positivo
        if 'salary' in data and data['salary'] <= 0:
            raise serializers.ValidationError({
                "salary": "El salario debe ser mayor que 0"
            })

        return data