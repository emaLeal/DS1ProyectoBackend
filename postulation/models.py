from django.db import models
from job_offer.models import JobOffer
from users.models import User
# Create your models here.


class Postulation(models.Model):
    applicant_document = models.ForeignKey(User, on_delete=models.CASCADE, to_field="document_id")
    job_offer_id = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    undergraduate_title = models.TextField()
    postgraduate_title = models.TextField(null=True, blank=True)
    motivation = models.TextField()
    resume = models.TextField()
    phone = models.CharField(max_length=15)
    application_date = models.DateField()
    
    class Meta:
        db_table = "Postulation"

    def __str__(self):
        return self.applicant_document
