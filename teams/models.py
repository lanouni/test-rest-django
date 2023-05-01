from django.db import models
from person.models import Person

# Create your models here.

class Teams(models.Model):
    name = models.CharField(max_length=100, unique=True)
    Fullname = models.CharField(max_length=100, null=True)


    #foreign key for manager (person)
    manager = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    deleted = models.BooleanField(default=False)