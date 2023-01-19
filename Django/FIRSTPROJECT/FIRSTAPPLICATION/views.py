from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return render(request, 'FIRSTAPPLICATION/index.html')

def AllStudentDetails(request):
    try:
        all_students = Student.objects.all()
    except:
        return HttpResponse('NOT FOUND', status = 404)
    if request.method == 'GET':
        students = StudentSerializer(all_students, many = True)
        return JsonResponse(students.data, safe = False)
