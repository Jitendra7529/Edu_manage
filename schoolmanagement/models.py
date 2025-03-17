from django.db import models

# Create your models here.

class Teacher(models.Model):
    firstname = models.CharField(max_length = 10, blank=False)
    lastname = models.CharField(max_length = 10, blank=False)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
class Student(models.Model):
    firstname = models.CharField(max_length = 8, blank=False)
    lastname = models.CharField(max_length = 9, blank=False )

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Subject(models.Model):
    name = models.CharField(max_length = 20, blank=False)

    def __str__(self):
        return self.name