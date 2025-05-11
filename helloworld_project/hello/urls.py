from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('student', views.get_Students, name='get_students'),
    path('student/<int:pk>/',views.StudentDetailView, name='studentdetail'),
]
