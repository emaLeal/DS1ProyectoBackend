from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from job_offer.models import JobOffer
from job_offer.serializers import JobOfferSerializer

# Create your views here.

# # 1. Get all job offers
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_all_job_offers(request):
#     """Returns all available job offers."""
#     offers = JobOffer.objects.all()
#     serializer = JobOfferSerializer(offers, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# # 2. Get a specific job offer by ID
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_job_offer_by_id(request, id_ofer):
#     """Returns a job offer by its ID."""
#     try:
#         offer = JobOffer.objects.get(id_ofer=id_ofer)
#         serializer = JobOfferSerializer(offer)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except JobOffer.DoesNotExist:
#         return Response({"error": "Job offer not found"}, status=status.HTTP_404_NOT_FOUND)


# # 3. Update a job offer by ID
# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def update_job_offer(request, id_ofer):
#     """Updates an existing job offer."""
#     try:
#         offer = JobOffer.objects.get(id_ofer=id_ofer)
#         serializer = JobOfferSerializer(offer, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     except JobOffer.DoesNotExist:
#         return Response({"error": "Job offer not found"}, status=status.HTTP_404_NOT_FOUND)


# # 4. Delete a job offer by ID
# @api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
# def delete_job_offer(request, id_ofer):
#     """Deletes a job offer by ID."""
#     try:
#         offer = JobOffer.objects.get(id_ofer=id_ofer)
#         offer.delete()
#         return Response({"message": "Job offer deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
#     except JobOffer.DoesNotExist:
#         return Response({"error": "Job offer not found"}, status=status.HTTP_404_NOT_FOUND)


# # 5. Create a new job offer
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_job_offer(request):
#     """Creates a new job offer."""
#     serializer = JobOfferSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)