from django.db import models

# Create your models here.
class Role(models.Model):
    id = models.AutoField(primary_key=True)
    ROLE_CHOICE= [
        ("A","Admin"),
        ("U", "User"),
        ("M","Manager")
    ]
    name = models.CharField(max_length=10, choices=ROLE_CHOICE)