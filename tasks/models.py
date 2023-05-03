from django.db import models

# Create your models here.

class Tasks(models.Model):
   STATUS_CHOICES = [
      ("I","In progress"),
      ("P","Planned"),
      ("C","Closed"),
      ("A","Audit"),
   ]
   TYPE_CHOICES = [
      ("P", "Prod"),
      ("E", "Enhacement"),
      ("Pr", "Project"),
      ("S", "Support"),
   ]
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=150)
   description = models.TextField(null = True)
   startdate = models.DateField(null=True)
   enddate = models.DateField(null=True)
   commentaire = models.TextField(null=True)
   sponsor = models.CharField(max_length=50, null=True)
   chargefte = models.FloatField()
   deleted = models.BooleanField(default=False)
   statut = models.CharField(choices=STATUS_CHOICES, default="In progress")
   type = models.CharField(choices=TYPE_CHOICES, default="Prod")
   task = models.ForeignKey('tasks.Tasks', on_delete=models.CASCADE, null=True)
   niveau = models.CharField(null=True)