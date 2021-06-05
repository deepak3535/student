from django.db import models
from django.db.models.fields import CharField,TextField
# Create your models here.
class stud(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    age=models.IntegerField()
    grade=models.IntegerField()
    address=models.TextField(max_length=100)
    parent_occupation=models.CharField(max_length=100)

    def __str__(self):
        return self.firstname