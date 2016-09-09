from django.db import models


# Create your models here.

class Partner(models.Model):
    pid = models.AutoField(primary_key=True)
    partner = models.CharField("Name :", max_length=30)
    contact = models.IntegerField("Contact No. :")
    email = models.EmailField("Email id :")
    coordinatorName = models.CharField("Coordinator :", max_length=30)
    location = models.CharField("Location:", max_length=10)
    address = models.CharField("Address :", max_length=160)
    spl = models.CharField("Specializations :", max_length=30)
    SoS = models.IntegerField("Seats per slot :")
    remark = models.TextField("Remark :")


class WorkingDay(models.Model):
    WORKING_DAYS = (
        ('Su', 'Sunday'),
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wednesday'),
        ('Th', 'Thursday'),
        ('F', 'Friday'),
        ('S', 'Saturday'),
    )
    partner = models.ForeignKey(Partner)  # Each partner has multiple working days
    workingDay = models.CharField(max_length=2, choices=WORKING_DAYS)


class TimeSlots(models.Model):
    time = models.ForeignKey(WorkingDay)  # Each working day has multiple time slots
    timeSlots = models.TimeField()


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
    firstName = models.CharField("First Name :", max_length=20)
    lastName = models.CharField("Last Name :", max_length=20)
    dob = models.DateField("Date of birth :")
    gender = models.CharField("Gender :", max_length=1, choices=GENDER)
    Sap = models.IntegerField("SAP id :")
    email = models.EmailField("Email id :")
    phone = models.IntegerField("Phone Number :")
    division = models.CharField("Division :", max_length=1)
    year = models.IntegerField("Year :", choices=YEAR)
    course = models.CharField("Course :", choices=COURSE, max_length=10)
    stream = models.CharField("Stream :", choices=STREAM, max_length=10)


class PaymentConfirmation(models.Model):
    PAYMENT = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    member = models.ForeignKey(MemberDetails)
    payment = models.CharField(max_length=1, choices=PAYMENT)


class Curriculum(models.Model):
    partner = models.ForeignKey(Partner)
    curriculum = models.TextField("Curriculum :")


'''class SelectPartner(models.Model):
    member = models.ForeignKey(MemberDetails)
    partner = models.ForeignKey(PartnerDetails)
    day = models.ForeignKey(WorkingDay)
    time = models.ForeignKey(TimeSlots)
'''
