from django.urls import path

from . import views

urlpatterns = [
    path('prueba/', views.prueba),
    path('getall/', views.get_all_job_offers),
    path('get/<int:id_ofer>/', views.get_job_offer_by_id),
    path('put/<int:id_ofer>/', views.update_job_offer),
    path('delete/<int:id_ofer>/', views.delete_job_offer),
    path('post/', views.create_job_offer),
]
