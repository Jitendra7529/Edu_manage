from django.contrib import admin

# Register your models here.
from .models import Teacher, Student, Subject
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)