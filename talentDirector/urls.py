from django.urls import path
from . import views

urlpatterns = [
    path('getall/', views.get_all_talent_directors),
    path('get/<int:document_id>/', views.get_talent_director_by_id),
    path('create/', views.create_talent_director),
    path('update/<int:document_idd>/', views.update_talent_director),
    path('delete/<int:document_id>/', views.delete_talent_director),
]
