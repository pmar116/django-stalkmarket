from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator
import datetime

class Stalk(models.Model):
    pub_date = models.DateTimeField("Date Published", default=datetime.datetime.now)
    price = models.IntegerField(validators=[MaxValueValidator(1000)])
    user = models.CharField(max_length=50)
    DodoCode = models.CharField(max_length=50, blank=True)

    def get_absolute_url(self):
        return reverse('stalkmarket')

class Trade(models.Model):
    pub_date = models.DateTimeField("Date Published", default=datetime.datetime.now)
    item = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    DodoCode = models.CharField(max_length=50, blank=True)

    def get_absolute_url(self):
        return reverse('trade')