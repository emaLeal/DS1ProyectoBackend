# views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status  # ✅ Agregado import
from django.db.models import Q
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsAdminUser
from django.db import IntegrityError

User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    '''Recieves the code and password from a user and returns a token'''
    print(request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        print("entro")
        serializer.save()
        user = User.objects.get(document_id=request.data['document_id'])
        user.set_password(request.data['password'])
        user.save()
        return Response({'message': f'User {user} successfully created'}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    profile_user = request.user
    serializer = UserSerializer(instance=profile_user)
    return Response(serializer.data, status=200)

@api_view(['GET'])
# @permission_classes([IsAdminUser])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(instance=users, many=True)
    return Response(serializer.data, status=200)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])  # ✅ Agregado permiso
def update_user(request, document_id):
    try:
        user = User.objects.get(document_id=document_id)
    except User.DoesNotExist:
        return Response({'detail': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user, data=request.data, partial=True)  # ✅ Agregado partial=True
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])  # ✅ Agregado permiso
def delete_user(request, document_id):
    try:
        user = User.objects.get(document_id=document_id)
    except User.DoesNotExist:
        return Response({'detail': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    try:
        user.delete()
        return Response({'detail': 'Usuario eliminado exitosamente'}, status=status.HTTP_200_OK)
    except IntegrityError as e:
        return Response({'detail': f'No se puede eliminar el usuario: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
