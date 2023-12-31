from django.db import models


# Create your models here.
# Add univer and consult workers
class User(models.Model):
    ID_raqam = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    is_univer = models.BooleanField(default=False)

    def __str__(self):
        return self.ID_raqam


# Add students 
class Clients(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    consulting = models.CharField(max_length=2500, default='')  # Set a default value
    surname = models.CharField(max_length=200, null=True, blank=True)
    father_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    diploma = models.FileField(upload_to='diplomas/', blank=True, null=True)
    picture = models.FileField(upload_to='pictures/', blank=True, null=True)
    certificates = models.FileField(upload_to='certificates/', blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True)
    pasport_seria = models.CharField(max_length=3, blank=True)
    pasport_raqam = models.IntegerField(null=True, blank=True)
    is_student = models.BooleanField(default = False)
    university = models.CharField(max_length=200, blank=True, default='')  # Set a default value
    faculty = models.CharField(max_length=200, blank=True, default='')  # Set a default value
    study_time = models.CharField(max_length=2500, blank=True, default='')  # Set a default value

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
    ID_raqam = models.CharField(max_length=2500)
    place = models.CharField(max_length=2500)
    time_study = models.CharField(max_length=250, choices=study)
    bio = models.CharField(max_length =50000)
    date_begin = models.DateField()
    mission = models.CharField(max_length = 50000)

    def __str__(self) -> str:
        return self.name

    def formatted_date(self):
        return self.date_begin.strftime('%d-%m-%Y')


# Add New Consulting(for new branch)
class Consulting(models.Model):
    place = models.CharField(max_length=2500)
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=25000)
    ID_raqam = models.CharField(max_length=2500)
    director = models.CharField(max_length=2500)
    place_office = models.CharField(max_length=25000000)

    def __str__(self):
        return self.name
