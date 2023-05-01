from django.db import models
from role.models import Role
from tasks.models import Tasks
#from teams.models import Teams

# Create your models here.
class Person(models.Model):
    GENDER_CHOICE = [
        ("H", "Homme"),
        ("F", "Female")
    ]

    name = models.CharField(max_length=50, )
    lastName = models.CharField(max_length=50, )
    email = models.CharField(max_length=32, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    date_arrivee = models.DateField(null=True)
    date_depart = models.DateField(null=True)
    role = models.ForeignKey(Role , on_delete=models.CASCADE)
    team = models.ForeignKey('teams.Teams', on_delete=models.CASCADE, null=True)
    deleted = models.BooleanField(default=False)


class TaskByPerson(models.Model):
    task = models.ForeignKey(Tasks,on_delete=models.CASCADE, default=1)
    # foreign key of person
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

class Track(models.Model):

    nbrheures = models.FloatField(null=True)
    date = models.DateField(null=True)
    task = models.ForeignKey(TaskByPerson,on_delete=models.CASCADE, default=1)

    created_at = models.DateTimeField(auto_now_add=True)