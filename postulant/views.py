
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Postulant
from .serializers import PostulantSerializer

# Create your views here.

# 1. Obtener todos los postulantes
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_postulants(request):
    """Returns all postulants."""
    postulants = Postulant.objects.all()
    serializer = PostulantSerializer(postulants, many=True)
    return Response(serializer.data, status=200)


# 2. Obtener un postulante por ID
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_postulant_by_id(request, document_id):
    """Returns a postulant by document ID."""
    try:
        postulant = Postulant.objects.get(document_id=document_id)
        serializer = PostulantSerializer(postulant)
        return Response(serializer.data, status=200)
    except Postulant.DoesNotExist:
        return Response({"error": "Postulant not found"}, status=404)


# 3. Actualizar un postulante por ID
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_postulant(request, document_id):
    """Updates an existing postulant."""
    try:
        postulant = Postulant.objects.get(document_id=document_id)
        serializer = PostulantSerializer(postulant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    except Postulant.DoesNotExist:
        return Response({"error": "Postulant not found"}, status=404)


# 4. Eliminar un postulante por ID
@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def delete_postulant(request, document_id):
    """Deletes a postulant by document ID."""
    try:
        postulant = Postulant.objects.get(document_id=document_id)
        postulant.delete()
        return Response({"message": "Postulant deleted successfully"}, status=204)
    except Postulant.DoesNotExist:
        return Response({"error": "Postulant not found"}, status=404)


# 5. Crear un nuevo postulante
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_postulant(request):
    """Creates a new postulant."""
    serializer = PostulantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
