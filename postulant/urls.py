from django.urls import path
from . import views

urlpatterns = [
    path('getall/', views.get_all_postulants),
    path('get/<int:document_id>/', views.get_postulant_by_id),
    path('put/<int:document_id>/', views.update_postulant),
    path('delete/<int:document_id>/', views.delete_postulant),
    path('create/', views.create_postulant),

]
