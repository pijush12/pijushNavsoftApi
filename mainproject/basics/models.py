from django.db import models

# Create your models here.

class Student(models.Model):
    StudentId=models.AutoField(primary_key=True)
    StudentName=models.CharField(max_length=100)
    Roll=models.IntegerField()
    Department=models.CharField(max_length=100)
    
    def  __str__(self):
        return self.StudentName