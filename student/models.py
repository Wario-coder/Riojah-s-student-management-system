from django.db import models

# Create your models here.
class Students(models.Model):
    student_number=models.PositiveIntegerField()
    First_name=models.CharField(max_length=30)
    Last_name=models.CharField(max_length=30)
    Email=models.CharField(max_length=100)
    Field_of_study=models.CharField(max_length=50)
    GPA=models.FloatField()

def _str_(self):
    return f'Students: {self.First_name} {self.Last_name}'
    
