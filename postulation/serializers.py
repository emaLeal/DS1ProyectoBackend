from rest_framework import serializers
from .models import Postulation
from drf_extra_fields.fields import Base64FileField
import os
import io
import PyPDF2
from PyPDF2.errors import PdfReadError
from django.core.files.base import ContentFile

class PDFBase64File(Base64FileField):
    ALLOWED_TYPES = ['pdf']

    def get_file_extension(self, filename, decoded_file):
        try:
            # Intenta leer el archivo como PDF para verificar su validez
            reader = PyPDF2.PdfReader(io.BytesIO(decoded_file))
            if reader.pages:  # Si tiene páginas, es válido
                return 'pdf'
            raise PdfReadError("El archivo no contiene páginas PDF válidas.")
        except PdfReadError as e:
            raise serializers.ValidationError(f"Archivo PDF inválido: {e}")

class PostulationSerializer(serializers.ModelSerializer):
    resume_support = PDFBase64File()
    undergraduate_support = PDFBase64File(required=True)
    postgraduate_support = PDFBase64File(required=True)
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
            'application_date',
            'resume_support',
            'undergraduate_support',
            'postgraduate_support',
            
        ]

    def create(self, validated_data):
            applicant_document = validated_data.get('applicant_document')

            # Renombrar los archivos si están presentes
            for key in ['resume_support', 'undergraduate_support', 'postgraduate_support']:
                file = validated_data.get(key)
                if file:
                    # Extraer extensión (debería ser 'pdf')
                    ext = os.path.splitext(file.name)[1] or '.pdf'
                    # Generar nuevo nombre basado en applicant_document
                    new_name = f"{key}_{applicant_document}{ext}"
                    validated_data[key] = ContentFile(file.read(), name=new_name)

            return super().create(validated_data)