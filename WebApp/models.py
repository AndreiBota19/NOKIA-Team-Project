from django.db import models
from django.db import connection

# Create your models here.

class Faculty(models.Model):

    ID = models.CharField(primary_key=True, max_length=50)
    #adress = models.CharField(max_length=50)

    def __str__(self):
        return self.ID

    class Meta:
        db_table = "Faculty"

class FacultySpecializations(models.Model):

    ID = models.CharField(primary_key=True, max_length=25)

    def __str__(self):
        return self.ID

    class Meta:
        db_table = "FacultySpecializations"

class Students(models.Model):

    cnp = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)
    DoB = models.DateField()
    PoB = models.CharField(max_length=30)
    facultyName = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    specializationName = models.ForeignKey(FacultySpecializations, on_delete=models.CASCADE)
    sex = models.CharField(max_length=8)
    address = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=15)
    lastNameFather = models.CharField(max_length=15)
    lastNameMother = models.CharField(max_length=15)
    motherProfession = models.CharField(max_length=25)
    fatherProfession = models.CharField(max_length=25)
    fatherPhoneNumber = models.CharField(max_length=15)
    motherPhoneNumber = models.CharField(max_length=15)

    def __str__(self):
        return self.cnp

    class Meta:
        db_table = "Students"

    
    


    

    


