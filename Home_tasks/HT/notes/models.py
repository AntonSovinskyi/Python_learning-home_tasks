from django.db import models
from datetime import date


class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1000, default='')
    reminder = models.DateTimeField('date published')
    category = models.ForeignKey('Categories', related_name='note_category', on_delete=models.CASCADE)


class Categories(models.Model):
    title = models.CharField(max_length=200)
