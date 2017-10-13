import datetime

from django.db import models
from datetime import date
from django.utils import timezone
from django.core.validators import validate_comma_separated_integer_list


class Bet(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=200)
    bet_maker = models.CharField(max_length=200, default='maker')
    bet_taker = models.CharField(max_length=200, default='taker')
    complete = models.BooleanField(default=False)


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
