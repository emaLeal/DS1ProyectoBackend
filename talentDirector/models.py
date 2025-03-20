from django.db import models
from users.models import User
# Create your models here.
# Modelo de Director de Talento
class TalentDirector(models.Model):
    document_id = models.OneToOneField(
        User, on_delete=models.CASCADE, to_field="document_id", primary_key=True
    )
    description = models.TextField(default="", blank=True)

    class Meta:
        db_table = "TalentDirector"

    def __str__(self):
        return self.document_id