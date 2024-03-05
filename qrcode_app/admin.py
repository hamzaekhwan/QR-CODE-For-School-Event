from django.contrib import admin
from .models import *


class StudentAdmin(admin.ModelAdmin):
    list_filter= ('student_id',)
    search_fields=['student_name']

class InviteAdmin(admin.ModelAdmin):
    
    list_filter= ('position',)
    search_fields=['name']
admin.site.register(Student,StudentAdmin)
admin.site.register(Invite,InviteAdmin)