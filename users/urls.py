# urls.py
from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path('register/', views.register),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('get_profile/', views.get_profile),
    path('users/getall/', views.get_users),
    path('update/<str:document_id>/', views.update_user),  # ✅ Corregido
    path('delete/<str:document_id>/', views.delete_user),  # ✅ Corregido
    path('change_password/', views.change_password, name='change_password'),
    path('password_reset/', include('django_rest_passwordreset.urls'), name='password_reset')
]