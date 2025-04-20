from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import TalentDirector
from .serializers import TalentDirectorSerializer

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_talent_director(request):
    serializer = TalentDirectorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_talent_directors(request):
    directors = TalentDirector.objects.all()
    serializer = TalentDirectorSerializer(directors, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_talent_director_by_id(request, document_id):
    try:
        director = TalentDirector.objects.get(document_id=document_id)
        serializer = TalentDirectorSerializer(director)
        return Response(serializer.data, status=200)
    except TalentDirector.DoesNotExist:
        return Response({"error": "Talent Director not found"}, status=404)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_talent_director(request, document_id):
    try:
        director = TalentDirector.objects.get(document_id=document_id)
        serializer = TalentDirectorSerializer(director, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    except TalentDirector.DoesNotExist:
        return Response({"error": "Talent Director not found"}, status=404)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def delete_talent_director(request, document_id):
    try:
        director = TalentDirector.objects.get(document_id=document_id)
        director.delete()
        return Response({"message": "Talent Director deleted successfully"}, status=204)
    except TalentDirector.DoesNotExist:
        return Response({"error": "Talent Director not found"}, status=404)
