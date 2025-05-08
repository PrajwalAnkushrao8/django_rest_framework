from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
def get_skills(request):
    skills = [
        "python","Django","Docker","Kubernates","Jenkins"
    ]
    return HttpResponse(skills)