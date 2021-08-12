from django.http import request
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Students, Faculty, FacultySpecializations, Staff, StaffType
from django.contrib.auth.decorators import login_required



@login_required
def home(request):

    qs = Students.objects.all()
    qs_staff = Staff.objects.all()
    context = {
        'queryset' : qs,
        'queryset_staff' : qs_staff
    }

    return render(request, 'WebApp/home.html', context)


@login_required
def viewData(request):

    qs = Students.objects.all()
    qs_staff = Staff.objects.all()
    # attendance = Attendance.objects.all()
    # subjects = Subjects.objects.all()
    students_table=[]

    checkbox_id = request.GET.get('id_stud')
    checkbox_fn = request.GET.get('firstname_stud')
    checkbox_ln = request.GET.get('lastname_stud')
    checkbox_dob = request.GET.get('dob_stud')
    checkbox_pob = request.GET.get('pob_stud')
    checkbox_univ = request.GET.get('university_stud')
    checkbox_spec = request.GET.get('spec_stud')
    checkbox_gender = request.GET.get('gender_stud')
    checkbox_adr = request.GET.get('address_stud')
    checkbox_pm = request.GET.get('phonenumber_stud')
    checkbox_ffn = request.GET.get('ffname_stud')
    checkbox_mfn = request.GET.get('mfn_stud')

    if checkbox_id == 'on':
        students_table.append('studentID')

    if checkbox_fn == 'on':
        students_table.append('first_name')

    if checkbox_ln == 'on':
        students_table.append('lastname_stud')

    if checkbox_dob == 'on':
        students_table.append('date_of_birth')

    if checkbox_pob == 'on':
        students_table.append('place_of_birth')

    if checkbox_univ == 'on':
        students_table.append('university')

    if checkbox_spec == 'on':
        students_table.append('specialization')

    if checkbox_gender == 'on':
        students_table.append('gender')

    if checkbox_adr == 'on':
        students_table.append('address')

    if checkbox_pm == 'on':
        students_table.append('phone_number')

    if checkbox_ffn == 'on':
        students_table.append('father_firstName')

    if checkbox_mfn == 'on':
        students_table.append('mother_firstName')


    #_____________________________________ Student _____________________________________

    first_name_contains_query = request.GET.get('first_name_contains')

    last_name_contains_query = request.GET.get('last_name_contains')

    personal_id_is_query = request.GET.get('personal_id_is')

    university_contains_query = request.GET.get('university_contains')

    specialization_contains_query = request.GET.get('specialization_contains')

    exact_gender_query = request.GET.get('exact_gender')

    specialization_contains_query = request.GET.get('specialization_contains')

    placeofbirth_contains_query = request.GET.get('placeofbirth_contains')

    dateofbirth_contains_query = request.GET.get('dateofbirth_contains')

    address_contains_query = request.GET.get('address_contains')

    phoneNumber_query = request.GET.get('phoneNumber_contains')

    firstNameFather_query = request.GET.get('firstNameFather_contains')

    firstNameMother_query = request.GET.get('firstNameMother_contains')



    if first_name_contains_query != ' ' and first_name_contains_query is not None:
        qs = qs.filter(firstName__icontains=first_name_contains_query)

    if last_name_contains_query != ' ' and last_name_contains_query is not None:
        qs = qs.filter(lastName__icontains=last_name_contains_query)

    if personal_id_is_query != ' ' and personal_id_is_query is not None:
        qs = qs.filter(cnp__icontains=personal_id_is_query)

    if exact_gender_query != ' ' and exact_gender_query is not None:
        qs = qs.filter(sex__icontains=exact_gender_query)

    if university_contains_query != ' ' and university_contains_query is not None:
        qs = qs.filter(facultyName__ID__icontains=university_contains_query)

    if specialization_contains_query != ' ' and specialization_contains_query is not None:
        qs = qs.filter(specializationName__ID__icontains=specialization_contains_query)

    if placeofbirth_contains_query != ' ' and placeofbirth_contains_query is not None:
        qs = qs.filter(PoB__icontains=placeofbirth_contains_query)

    if dateofbirth_contains_query != ' ' and dateofbirth_contains_query is not None:
        qs = qs.filter(DoB__icontains=dateofbirth_contains_query)

    if address_contains_query != ' ' and address_contains_query is not None:
        qs = qs.filter(address__icontains=address_contains_query)

    if phoneNumber_query != ' ' and phoneNumber_query is not None:
        qs = qs.filter(phoneNumber__icontains=phoneNumber_query)

    if firstNameFather_query != ' ' and firstNameFather_query is not None:
        qs = qs.filter(firstNameFather__icontains=firstNameFather_query)

    if firstNameMother_query != ' ' and firstNameMother_query is not None:
        qs = qs.filter(firstNameMother__icontains=firstNameMother_query)


    #_____________________________________STAFF_____________________________________


    # first_name_contains_query_staff = request.GET.get('first_name_contains_staff')

    # last_name_contains_query_staff = request.GET.get('last_name_contains_staff')

    # personal_id_is_query_staff = request.GET.get('personal_id_is_staff')

    # university_contains_query_staff = request.GET.get('university_contains_staff')

    # specialization_contains_query_staff = request.GET.get('specialization_contains_staff')

    # exact_gender_query_staff = request.GET.get('exact_gender_staff')

    # specialization_contains_query_staff = request.GET.get('specialization_contains_staff')

    # placeofbirth_contains_query_staff = request.GET.get('placeofbirth_contains_staff')

    # address_contains_query_staff = request.GET.get('address_contains_staff')

    # phoneNumber_query_staff = request.GET.get('phoneNumber_contains_staff')

    # lastNameFather_query_staff = request.GET.get('lastNameFather_contains_staff')

    # lastNameMother_query_staff = request.GET.get('lastNameMother_contains_staff')

    # dateOfHiring_query_staff = request.GET.get('dateOfHiring_contains_staff')

    # yearsOfService_query_staff = request.GET.get('yearsOfService_contains_staff')

    # speciality_query_staff = request.GET.get('speciality_contains_staff')

    # staffLevel_staff = request.GET.get('staffLevel_contains_staff')



    # if first_name_contains_query_staff != ' ' and first_name_contains_query_staff is not None:
    #     qs_staff = qs_staff.filter(firstName__icontains=first_name_contains_query_staff)

    # if last_name_contains_query_staff != ' ' and last_name_contains_query_staff is not None:
    #     qs_staff = qs_staff.filter(lastName__icontains=last_name_contains_query_staff)

    # if personal_id_is_query_staff != ' ' and personal_id_is_query_staff is not None:
    #     qs_staff = qs_staff.filter(cnp__icontains=personal_id_is_query_staff)

    # if exact_gender_query_staff != ' ' and exact_gender_query_staff is not None:
    #     qs_staff = qs_staff.filter(sex__icontains=exact_gender_query_staff)

    # if university_contains_query_staff != ' ' and university_contains_query_staff is not None:
    #     qs_staff = qs_staff.filter(facultyName__ID__icontains=university_contains_query_staff)

    # if specialization_contains_query_staff != ' ' and specialization_contains_query_staff is not None:
    #     qs_staff = qs_staff.filter(specializationName__ID__icontains=specialization_contains_query_staff)

    # if placeofbirth_contains_query_staff != ' ' and placeofbirth_contains_query_staff is not None:
    #     qs_staff = qs_staff.filter(PoB__icontains=placeofbirth_contains_query_staff)

    # if address_contains_query_staff != ' ' and address_contains_query_staff is not None:
    #     qs_staff = qs_staff.filter(address__icontains=address_contains_query_staff)

    # if phoneNumber_query_staff != ' ' and phoneNumber_query_staff is not None:
    #     qs_staff = qs_staff.filter(phoneNumber__icontains=phoneNumber_query_staff)

    # if lastNameFather_query_staff != ' ' and lastNameFather_query_staff is not None:
    #     qs_staff = qs_staff.filter(lastNameFather__icontains=lastNameFather_query_staff)

    # if lastNameMother_query_staff != ' ' and lastNameMother_query_staff is not None:
    #     qs_staff = qs_staff.filter(lastNameMother__icontains=lastNameMother_query_staff)

    # if dateOfHiring_query_staff_query_staff != ' ' and dateOfHiring_query_staff is not None:
    #     qs_staff = qs_staff.filter(dateOfHiring__icontains=dateOfHiring_query_staff)

    # if yearsOfService_query_staff != ' ' and yearsOfService_query_staff is not None:
    #     qs_staff = qs_staff.filter(yearsOfService__icontains=yearsOfService_query_staff)

    # if speciality_query_staff != ' ' and speciality_query_staff is not None:
    #     qs_staff = qs_staff.filter(speciality__icontains=speciality_query_staff)

    # if staffLevel_staff != ' ' and staffLevel_staff is not None:
    #     qs_staff = qs_staff.filter(staffLevel__ID__icontains=staffLevel_staff)


#_____________________________________Attendance_____________________________________

    # ID_attendance = request.GET.get('ID_attendance_grade')

    # IDStudent_attendance = request.GET.get('idstudent_attendance')

    # attended = request.GET.get('attended')

    # dateWhenAttended = request.GET.get('dateWhenAttended_date')




    # if ID_attendance != ' ' and ID_attendance is not None:
    #     attendance_query = attendance_query.filter(ID__icontains=ID_attendance)

    # if IDStudent_attendance != ' ' and IDStudent_attendance is not None:
    #     attendance_query = attendance_query.filter(IDStudent__ID__icontains=IDStudent_attendance)

    # if attended != ' ' and attended is not None:
    #     attendance_query = attendance_query.filter(ID__icontains=attended)

    # if dateWhenAttended != ' ' and dateWhenAttended is not None:
    #     attendance_query = attendance_query.filter(ID__icontains=dateWhenAttended)

#_____________________________________Subjects_____________________________________


    # IDSubjects = request.GET.get('id-subjects')

    # Abbreviation = request.GET.get('abbreviation-subjects')

    # FacultyName = request.GET.get('faculty-name-subjects')

    # teacher = request.GET.get('teacher-subjects')


    # if IDSubjects != ' ' and IDSubjects is not None:
    #     subjects = subjects.filter(IDSubjects__icontains=IDSubjects)

    # if Abbreviation != ' ' and Abbreviation is not None:
    #     subjects = subjects.filter(Abbreviation__icontains=Abbreviation)

    # if FacultyName != ' ' and FacultyName is not None:
    #     subjects = subjects.filter(FacultyName__ID__icontains=FacultyName)

    # if teacher != ' ' and teacher is not None:
    #     subjects = subjects.filter(teacher__ID__icontains=teacher)





    context = {
        'queryset' : qs,
        'queryset_staff' : qs_staff,
        # 'attendance_query' : atttendance,
        # 'subjects_query' : subjects
        'students_table' : students_table

    }

    return render(request, 'WebApp/viewData.html', context)

@login_required
def about(request):
    students = Students.objects.all()
    return render(request, 'WebApp/about.html', {'student': students})

#def displayData(request):
#    result = display.objects.all()
#    return render(request, 'WebApp/about.html', {"display": result})
