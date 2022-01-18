from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from basics.models import Student
from basics.serializers import StudentSerializer
from django.core.files.storage import default_storage

@csrf_exempt
def StudentApi(request,id=None):
    if request.method=='GET':
        # students=Student.objects.all()
        # student_serializer=StudentSerializer(students,many=True)
        # return JsonResponse(student_serializer.data,safe=False)
        if id is not None:
            students=Student.objects.get(StudentId=id)
            student_serializer=StudentSerializer(students)
            return JsonResponse(student_serializer.data,safe=False)
        else:
            students=Student.objects.all()
            student_serializer=StudentSerializer(students,many=True)
            return JsonResponse(student_serializer.data,safe=False)    




        
    elif request.method=='POST':
        student_data=JSONParser().parse(request)
        student_serializer=StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Added Sucessfully",safe=False) 
        return JsonResponse("Failed to add",safe=False)

    elif request.method=='PUT':
        student_data=JSONParser().parse(request)
        student=Student.objects.get(StudentId=student_data['StudentId'])
        student_serializer=StudentSerializer(student,data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse('Updated Sucessfully',safe=False)
        return JsonResponse("Failed to update")
    elif request.method=='DELETE':
        student=Student.objects.get(StudentId=id)
        student.delete()
        return JsonResponse("Deleted Sucessfully", safe=False)   

