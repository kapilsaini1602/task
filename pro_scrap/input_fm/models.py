from django.db import models

# Create your models here.
class applicant_data(models.Model):
    center = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    booking_status = models.CharField(blank=True,max_length=20)

    class Meta:
        db_table = 'applicant_data'


