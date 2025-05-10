from django.shortcuts import render
from django.http import JsonResponse

from .serializers import EmployeeSerializer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Employee
from rest_framework.views import APIView

class Employees(APIView):
    def get(self,request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request):
        emp_data = request.data
        serializer = EmployeeSerializer(data = emp_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


