from django.db import models

class Student(models.Model):
    roll_no = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=40)

    def __str__(self):
        return self.name
