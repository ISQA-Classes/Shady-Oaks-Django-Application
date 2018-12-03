# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.


# Create your models here.
class Customer(models.Model):
    cust_name = models.CharField(max_length=50)
    organization = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    bldgroom = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    account_number = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.cust_name)


class Event(models.Model):
    event_name = models.CharField(blank=True, max_length=150)
    event_start = models.DateTimeField(default=timezone.now)
    event_end = models.DateTimeField(default=timezone.now)
    attendees = models.IntegerField(default=0)
    organization = models.CharField(blank=True, max_length=100)
    contact_number = models.CharField(blank=True, max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.event_name)


class Teetime(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    Teetime_Name = models.CharField(default="Tee Time", max_length=50)
    Teetime_Start = models.DateTimeField(default=timezone.now)
    Golf_Carts = models.IntegerField(default=0)
    Golfers_Allowed = models.IntegerField(default=1)
    Created_Date = models.DateTimeField(default=timezone.now)
    Updated_Date = models.DateTimeField(default=timezone.now)


    def created(self):
        self.Created_Date = timezone.now()
        self.save()

    def updated(self):
        self.Updated_Date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.Teetime_Name)






