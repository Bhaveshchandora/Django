from django.db import models

# Create your models here.
class book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    pages=models.IntegerField()
    price=models.IntegerField()
#now register in admin.py
