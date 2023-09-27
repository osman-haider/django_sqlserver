from django.db import models

class Employee(models.Model):
    EmployeeID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
