from django.db import models
from django.contrib.auth.models import AbstractUser
from role.models import Role
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser):
    '''Custom Model for an user in the platform, being admin, Human Managment's Director or Postulant'''
    
    username = None
    name = models.CharField(max_length=130, default="")
    last_name = models.CharField(max_length=130, default="")
    document_id = models.CharField(max_length=15, unique=True, default="", primary_key=True)
    phone = models.CharField(max_length=15, default="", blank=True)
    cell_phone = models.CharField(max_length=20, default="", blank=True)
    email = models.EmailField(max_length=100,unique=True, default="")
    is_active = models.BooleanField(default=True),
    birth_date = models.DateField(default='2000-01-01')
    address = models.CharField(max_length=200, default="")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default=3)
    gender = models.CharField(max_length=10, default="")
    identification_type = models.CharField(max_length=50, default="")
    
    REQUIRED_FIELDS = [
        'name',
        'last_name',
        'email',
        'phone',
        # 'role',
        'gender',
        'cell_phone',
        'birth_date'
        ]
    USERNAME_FIELD = 'document_id'
    # objects = CustomUserManager()

    class Meta:
        db_table = "User"
        
    def __str__(self):
        return self.document_id

