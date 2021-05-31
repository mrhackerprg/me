from django.db import models

# Create your models here.

class Info(models.Model):
    name_lastname = models.CharField(max_length = 150)
    bio = models.TextField()
    birth = models.CharField(max_length = 150)
    phone = models.IntegerField()
    address = models.TextField()
    e_email = models.CharField(max_length = 150)
    website = models.CharField(max_length = 150)

class Aboutme(models.Model):
    bio = models.TextField()
    about_me = models.TextField()

class Contactme(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    messages = models.TextField()