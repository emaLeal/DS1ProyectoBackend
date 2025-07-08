from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny 
from users.permissions import IsTalentDirector, IsAdminUser

from .models import JobOffer
from .serializers import JobOfferSerializer

# Create your views here.

@api_view(['GET'])
def prueba(request):
    return Response({"mensaje": "todo ok"})



# 1. Get all job offers
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_job_offers(request):
    """Returns all available job offers."""
    offers = JobOffer.objects.all()
    serializer = JobOfferSerializer(offers, many=True)
    return Response(serializer.data, status=200)


# 2. Get a specific job offer by ID
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_job_offer_by_id(request, id_ofer):
    """Returns a job offer by its ID."""
    try:
        offer = JobOffer.objects.get(id=id_ofer)
        serializer = JobOfferSerializer(offer)
        return Response(serializer.data, status=200)
    except JobOffer.DoesNotExist:
        return Response({"error": "Job offer not found"}, status=400)


# 3. Update a job offer by ID
@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_job_offer(request, id_ofer):
    """Updates an existing job offer."""
    try:
        offer = JobOffer.objects.get(id=id_ofer)
        serializer = JobOfferSerializer(offer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    except JobOffer.DoesNotExist:
        return Response({"error": "Job offer not found"}, status=404)


# 4. Delete a job offer by ID
@api_view(['DELETE'])
@permission_classes([IsAuthenticated,IsAdminUser])
def delete_job_offer(request, id_ofer):
    """Deletes a job offer by ID."""
    try:
        offer = JobOffer.objects.get(id=id_ofer)
        offer.delete()
        return Response({"message": "Job offer deleted successfully"}, status=status.HTTP_200_OK)
    except JobOffer.DoesNotExist:
        return Response({"error": "Job offer not found"}, status=404)


# 5. Create a new job offer
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def create_job_offer(request):
    # """Creates a new job offer."""
    serializer = JobOfferSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response({"mensaje": "todo ok"})