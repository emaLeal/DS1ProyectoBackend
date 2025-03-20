from django.db import models
from users.models import User


# Create your models here.
class Postulant(models.Model):
    document_id = models.OneToOneField(User, on_delete=models.CASCADE, to_field="document_id", primary_key=True)
    gender = models.CharField(max_length=10)
    identification_type = models.CharField(max_length=50)

    class Meta:
        db_table = "Postulant"

    def __str__(self):
        return self.document_id