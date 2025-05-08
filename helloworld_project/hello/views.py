from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


def hello_world(request):
    return HttpResponse("Hello World")

@api_view(['GET','POST'])
def get_Students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Student is saved successfully"}, status=status.HTTP_201_CREATED)
        print({"message":"error"},serializer.errors)
        return Response({"message":"Failed to save the student"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def StudentDetailView(request , pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)