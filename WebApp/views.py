from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Students, Faculty, FacultySpecializations





def home(request):
    qs = Students.objects.all()
    first_name_contains_query = request.GET.get('first_name_contains')
    last_name_contains_query = request.GET.get('last_name_contains')
    personal_id_is_query = request.GET.get('personal_id_is')
    university_contains_query = request.GET.get('university_contains')
    specialization_contains_query = request.GET.get('specialization_contains')
    exact_gender_query = request.GET.get('exact_gender')
    specialization_contains_query = request.GET.get('specialization_contains')

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


    context = {
        'queryset' : qs
    }
    
    return render(request, 'WebApp/home.html', context)

def about(request):
    students = Students.objects.all()
    return render(request, 'WebApp/about.html', {'student': students})

#def displayData(request):
#    result = display.objects.all()
#    return render(request, 'WebApp/about.html', {"display": result})





