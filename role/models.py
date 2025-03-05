from django.db import models

# Create your models here.
class Role(models.Model):
    '''Model for the role the user will be asigned with'''
    description = models.CharField(max_length=20, default="Postulant")