from django.db import models

class Info(models.Model):
    id = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=200)

class Flag(models.Model):
    flag = models.CharField(max_length=200)
