from django.db import models

# Create your models here.
# Add univer and consult workers
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    is_univer = models.BooleanField(default = False)

    def __str__(self):
        return self.username
    

# Add students 
class Clients(models.Model):
    name = models.CharField(max_length=200, null = True, blank=True)
    surname = models.CharField(max_length=200, null = True, blank=True)
    father_name = models.CharField(max_length=200, null = True, blank=True)
    email = models.CharField(max_length=500, null = True, blank=True)
    date = models.DateField(null=True, blank=True)
    diploma = models.FileField(upload_to='diplomas', blank=True)
    picture = models.FileField(upload_to='pictures', blank=True)
    certificates = models.FileField(upload_to='certificates', blank = True, null = True)
    phone = models.CharField(max_length=200, blank=True)
    pasport_seria = models.CharField(max_length=3, blank=True)
    pasport_raqam = models.IntegerField(null = True, blank=True)
    university = models.CharField(max_length=200, blank=True)
    faculty = models.CharField(max_length=200, blank=True)
    study_time = models.CharField(max_length=2500, blank =True)

    def __str__(self):
        return self.name
    

# Add New Universities which worked with
class University(models.Model):
    study = (
        ('kunduzgi', 'kunduzgi'),
        ('sirtqi', 'sirtqi'),
        ('kechki', 'kechki'),
    )
    name = models.CharField(max_length=2500)
    faculty = models.CharField(max_length=250)
    time_study = models.CharField(max_length = 250, choices=study)

    def __str__(self) -> str:
        return self.name

