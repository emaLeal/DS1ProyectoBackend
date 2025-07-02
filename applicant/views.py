from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from users.permissions import IsAdminUser, IsTalentDirector
from rest_framework.response import Response
from rest_framework import status
from users.serializers import UserSerializer

User = get_user_model()
applicants = User.objects.filter(role=3)

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_applicants(request):
    print(applicants)
    serializer = UserSerializer(applicants, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_applicant(request, document_id):
    applicant = applicants.filter(document_id=document_id)
    if len(applicant) == 0:
        return Response({'error': f'No se encontró postulante con la cedula {document_id}'}, status=404)
    serializer = UserSerializer(applicant)
    return Response(serializer.data, status=200)


