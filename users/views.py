from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models import Q
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsAdminUser

User = get_user_model()

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    '''Recieves the code and password from a user and returns a token'''
    print(request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        print("entro")
        serializer.save()
        user = User.objects.get(document_id=serializer.data['document_id'])
        user.set_password(serializer.data['password'])
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
@permission_classes([IsAdminUser])
def get_users(request):
    users = User.objects.filter(Q(role_id=1) | Q(role_id=2))
    serializer = UserSerializer(instance=users, many=True)
    return Response(serializer.data, status=200)
