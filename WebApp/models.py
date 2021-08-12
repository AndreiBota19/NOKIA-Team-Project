from django.db import models
from django.db import connection
from django.db.models.deletion import CASCADE

# Create your models here.

class Faculty(models.Model):

    ID = models.CharField(primary_key=True, max_length=50)
    #adress = models.CharField(max_length=50, default="")

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

class StaffType(models.Model):

    ID = models.CharField(primary_key=True, max_length=25)

    def __str__(self):
        return self.ID

    class Meta:
        db_table = "StaffType"


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


class Staff(models.Model):

    cnp = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)
    PoB = models.DateField()
    DoB = models.CharField(max_length=30)
    facultyName = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    specializationName = models.ForeignKey(FacultySpecializations, on_delete=models.CASCADE)
    sex = models.CharField(max_length=8)
    address = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=15)
    lastNameFather = models.CharField(max_length=15)
    lastNameMother = models.CharField(max_length=15)
    dateOfHiring = models.DateField()
    salary = models.IntegerField()
    yearsOfService = models.IntegerField()
    speciality = models.CharField(max_length=35)
    staffLevel = models.ForeignKey(StaffType, on_delete=models.CASCADE)

    def __str__(self):
        return self.cnp

    class Meta:
        db_table = "Staff"


# class Attendance(models.Model):

#     ID = models.IntegerField(primary_key=True)
#     IDStudent = models.ForeignKey(Students, on_delete=models.CASCADE)
#     attended = models.BooleanField()
#     dateWhenAttended = models.DateField()

#     def __str__(self):
#         return self.ID

#     class Meta:
#         db_table = "Attendance"



# class Subjects(models.Model):

#     ID = models.CharField(primary_key=True, max_length=25)
#     Abbreviation = models.CharField(max_length=5)
#     FacultyName = models.ForeignKey(Faculty, on_delete=models.CASCADE)
#     teacher = models.ForeignKey(Staff, on_delete=models.CASCADE)


#     def __str__(self):
#         return self.ID

#     class Meta:
#         db_table = 'Subjects'
