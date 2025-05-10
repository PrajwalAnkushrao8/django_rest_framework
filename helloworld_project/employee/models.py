from django.db import models

class Employee(models.Model):
    emp_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254,unique=True,blank=True,null=True)


    def __str__(self):
        return self.name