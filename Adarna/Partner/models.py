from django.db import models


# Create your models here.
class PartnerDetails(models.Model):
    WORKING_DAYS = (
        ('Su', 'Sunday'),
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wednesday'),
        ('Th', 'Thursday'),
        ('F', 'Friday'),
        ('S', 'Saturday'),
    )
    name = models.CharField("Name :", max_length=30)
    contact = models.IntegerField("Contact No. :")
    email = models.EmailField("Email id :")
    cname = models.CharField("Coordinator :", max_length=30)
    location = models.CharField("Location:")
    address = models.CharField("Address :")
    spl = models.CharField("Specializations :")
    NoOfSeats = models.IntegerField("Number of Seats :")
    WorkingDays = models.CharField(max_length=2, choices=WORKING_DAYS)  # yet to complete


class MemberDetails(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    YEAR = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    COURSE = (
        ('MBA(Tech)', 'MBATech'),
        ('BTech', 'BTech'),
    )
    STREAM = (
        ('IT', 'IT'),
        ('CS', 'CS'),
        ('EXTC', 'EXTC'),
        ('Civil', 'Civil'),
        ('Chemical', 'Chemical'),
        ('Mechanical', 'Mechanical'),
    )
    UUID = models.IntegerField(primary_key=True)
    fname = models.CharField("First Name :", max_length=20)
    lname = models.CharField("Last Name :", max_length=20)
    dob = models.DateField("Date of birth :")
    gender = models.CharField("Gender :", max_length=1, choices=GENDER)
    Sap = models.IntegerField("SAP id :", max_length=11)
    email = models.EmailField("Email id :")
    phone = models.IntegerField("Phone Number :", max_length=10)
    division = models.CharField("Division :", max_length=1)
    year = models.IntegerField("Year :", choices=YEAR)
    course = models.CharField("Course :", choices=COURSE)
    stream = models.CharField("Stream :", choices=STREAM)

