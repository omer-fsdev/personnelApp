from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


TITLE = (("Team Lead", "L"), ("Developer", "D"), ("Tester", "T"))
GENDER = (("Female", "F"), ("Male", "M"), ("Prefer not to say", "N"))


class Personnel(models.Model):
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, related_name="personnel"
    )
    create_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20, choices=GENDER)
    salary = models.IntegerField(default=2000)
    start_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, choices=TITLE)

    def __str__(self):
        return self.first_name
