from django.urls import path
from . import views

urlpatterns = [
  path("get_all/",views.Employees.as_view()),
  path("employee/<int:pk>/",views.EmployeesDetails.as_view())
]
