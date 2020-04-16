from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator
from django.utils import timezone
import datetime
from . import helper


class Stalk(models.Model):
    pub_date = models.DateTimeField("Date Published", default=datetime.date.today())
    pub_time = models.DateTimeField("Time Published", default=timezone.now)
    morning = models.BooleanField(default=helper.ismorning())
    price = models.IntegerField(validators=[MaxValueValidator(1000)])
    user = models.CharField(max_length=50)
    DodoCode = models.CharField(max_length=50, blank=True)
    
    def get_absolute_url(self):
        return reverse('stalkmarket')

class Trade(models.Model):
    pub_date = models.DateTimeField("Date Published", default=datetime.date.today())
    pub_time = models.DateTimeField("Time Published", default=timezone.now)
    item = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    DodoCode = models.CharField(max_length=50, blank=True)

    def was_published_recently(self):
        return self.pub_time >= datetime.datetime.now() - datetime.timedelta(days=14)
    
    def get_absolute_url(self):
        return reverse('trade')
