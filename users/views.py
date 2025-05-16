from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny

User = get_user_model()

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    '''Recieves the code and password from a user and returns a token'''
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
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
    profile_raw = {
        'name': profile_user.name,
        'last_name': profile_user.last_name,
        'document_id': profile_user.document_id,
        'role': profile_user.role_id,
        'gender': profile_user.gender,
        'email': profile_user.email,
        'address': profile_user.address
    }
    return Response({'user': profile_raw}, status=200)


