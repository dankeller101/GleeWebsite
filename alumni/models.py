from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Member(models.Model):
    first_name  = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name

#used to list people who want access for admin
class unapprovedMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name  = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    authorized_code = models.CharField(null=True, max_length=100)
    date_refresh = models.DateField(null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class City(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Conductor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Chorus(models.Model):
    name = models.CharField(max_length=200)
    style = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    members = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return self.name





