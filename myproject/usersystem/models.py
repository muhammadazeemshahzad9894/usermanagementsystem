from django.db import models

class Users(models.Model):
    user_id = models.AutoField
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    cnic = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=25)
    password = models.CharField(max_length=25)


    def __str__(self):
        return self.firstname
