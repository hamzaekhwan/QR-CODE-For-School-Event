from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=50 , blank=True, null=True)
    student_name=models.CharField(max_length=50 , blank=True, null=True)

class Invite(models.Model):
    student_id = models.CharField(max_length=50 , blank=True, null=True, verbose_name='Student ID')
    name = models.CharField(max_length=50 , blank=True, null=True, verbose_name='name')
    position=models.CharField(max_length=50 , blank=True, null=True, verbose_name='Position')

    academic_level = models.CharField(max_length=50 , blank=True, null=True, verbose_name='Academic Level')

    first_companion = models.CharField(max_length=50 , blank=True, null=True, verbose_name='First Companion')
    first_companion_number = models.CharField(max_length=50 , blank=True, null=True, verbose_name='First Companion number')
    
    second_companion = models.CharField(max_length=50 , blank=True, null=True, verbose_name='Second Companion')
    second_companion_number = models.CharField(max_length=50 , blank=True, null=True, verbose_name='Second Companion number')

    invite_image=models.ImageField(null=True, blank=True
                         )
    first_companion_invite_image=models.ImageField(null=True, blank=True
                             )
    second_companion_invite_image=models.ImageField(null=True, blank=True
                           )
    
    invite_image_read=models.BooleanField(default=False)
    first_companion_read=models.BooleanField(default=False)
    second_companion_read=models.BooleanField(default=False)

    link1 = models.URLField(blank=True, null=True, verbose_name='Link1')
    link2 = models.URLField(blank=True, null=True, verbose_name='Link2')
    link3 = models.URLField(blank=True, null=True, verbose_name='Link3')

    def __str__(self):
        return self.name + "  " + str(self.id)

  
