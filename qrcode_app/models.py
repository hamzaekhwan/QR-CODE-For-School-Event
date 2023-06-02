from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=50 , blank=True, null=True)
    student_name=models.CharField(max_length=50 , blank=True, null=True)

class Invite(models.Model):  
    student_id = models.CharField(max_length=50 , blank=True, null=True)
    student_name=models.CharField(max_length=50 , blank=True, null=True)
    academic_level=models.CharField(max_length=50 , blank=True, null=True)
    first_companion=models.CharField(max_length=50 , blank=True, null=True)
    second_companion=models.CharField(max_length=50 , blank=True, null=True)
    invite_image=models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    
