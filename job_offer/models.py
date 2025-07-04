from django.db import models
from users.models import User
from django.db import models

class JobOffer(models.Model):
    title = models.CharField(max_length=255)
    responsibilities = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    education_level = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50)
    rank = models.CharField(max_length=10)
    other_requirements = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    talent_director_document = models.ForeignKey(User, on_delete=models.CASCADE, to_field="document_id")

    class Meta:
        db_table = "JobOffer"

    def __str__(self):
        return self.title
