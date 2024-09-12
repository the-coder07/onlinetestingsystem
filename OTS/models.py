from unittest.util import _MAX_LENGTH
from django.db import models

class Question(models.Model):
    qno=models.IntegerField(primary_key=True,auto_created=True)
    que=models.CharField(max_length=200)
    optiona=models.CharField(max_length=100)
    optionb=models.CharField(max_length=100)
    optionc=models.CharField(max_length=100)
    optiond=models.CharField(max_length=100)
    answer=models.CharField(max_length=1)
    
class User(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)
    role=models.CharField(max_length=20)
    realname=models.CharField(max_length=40)

class History(models.Model):
    date=models.DateTimeField(auto_now=False, auto_now_add=False)
    user=models.CharField(max_length=20)
    score=models.IntegerField()



