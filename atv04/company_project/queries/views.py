from django.http import JsonResponse
from .models import Employee, Position
from django.db.models import F, Count

# Query A
def query_a(request):
    employees = list(
        Employee.objects.select_related('position').order_by('hire_date').values(
            employee_name=F('name'),          
            position_title=F('position__title'),  
            admission_date=F('hire_date')    
        )
    )
    return JsonResponse(employees, safe=False, json_dumps_params={'ensure_ascii': False})


# Query B
def query_b(request):
    oldest_employee = (
        Employee.objects.select_related('position')
        .order_by('hire_date') 
        .values(
            employee_name=F('name'),         
            position_title=F('position__title')  
        )
        .first()  
    )
    return JsonResponse(oldest_employee, safe=False, json_dumps_params={'ensure_ascii': False})


# Query C
def query_c(request):
    positions = list(Position.objects.annotate(employee_count=Count('employees')).values(
        position=F('title'),
        employee_count=F('employee_count')
    ))
    return JsonResponse(positions, safe=False, json_dumps_params={'ensure_ascii': False})
