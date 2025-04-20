from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Postulation
from .serializers import PostulationSerializer

# Obtener todas las postulaciones
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_postulations(request):
    postulations = Postulation.objects.all()
    serializer = PostulationSerializer(postulations, many=True)
    return Response(serializer.data, status=200)



# Obtener una postulación por ID
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_postulation_by_id(request, id):
    try:
        postulation = Postulation.objects.get(id=id)
        serializer = PostulationSerializer(postulation)
        return Response(serializer.data, status=200)
    except Postulation.DoesNotExist:
        return Response({"error": "Postulation not found"}, status=404)

# Crear una nueva postulación
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_postulation(request):
    serializer = PostulationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Actualizar una postulación
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_postulation(request, id):
    try:
        postulation = Postulation.objects.get(id=id)
        serializer = PostulationSerializer(postulation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    except Postulation.DoesNotExist:
        return Response({"error": "Postulation not found"}, status=404)

# Eliminar una postulación
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_postulation(request, id):
    try:
        postulation = Postulation.objects.get(id=id)
        postulation.delete()
        return Response({"message": "Postulation deleted successfully"}, status=204)
    except Postulation.DoesNotExist:
        return Response({"error": "Postulation not found"}, status=404)
