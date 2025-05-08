from django.urls import path
from . import views

urlpatterns = [
    path('skills/', views.get_skills, name='get_skills'),
]
