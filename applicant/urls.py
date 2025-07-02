from django.urls import path
from . import views

urlpatterns = [
    path('getall/', views.get_applicants),
    path('get/<int:document_id>/', views.get_applicant)
]
