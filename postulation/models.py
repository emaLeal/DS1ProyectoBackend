from django.db import models
from job_offer.models import JobOffer
from users.models import User
from django.core.validators import FileExtensionValidator
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Postulation(models.Model):
    applicant_document = models.ForeignKey(User, on_delete=models.CASCADE, to_field="document_id")
    job_offer_id = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    undergraduate_title = models.TextField()
    postgraduate_title = models.TextField(null=True, blank=True)
    motivation = models.TextField(default="")
    resume = models.TextField(default="")
    resume_support = models.FileField(upload_to='curriculums/',
                                      validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    undergraduate_support = models.FileField(upload_to="undergraduate/",
                                            validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    postgraduate_support = models.FileField(upload_to="postgraduate/", 
                                            validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    phone = models.CharField(max_length=15)
    application_date = models.DateTimeField()
    
    class Meta:
        db_table = "Postulation"

    def __str__(self):
        return self.applicant_document
