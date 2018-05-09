"""
Definition of models.
"""

from django.db import models
from django.forms import ModelForm
from django.utils import timezone

# Create your models here.

class restaurants(models.Model):
    name = models.CharField(max_length = 50, default='')
    address = models.CharField(max_length = 50, default='')
    city = models.CharField(max_length = 50, default='')
    state = models.CharField(max_length = 2, default='')
    zip = models.CharField(max_length=50, default='')

class rtemptime(models.Model):
    Temp_wait_time = models.IntegerField()
    created = models.DateTimeField(auto_now=True)

class RenterForm(ModelForm):
    class Meta :
        model = rtemptime
        fields = ['Temp_wait_time']