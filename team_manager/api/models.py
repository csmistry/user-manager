from django.db import models
from django.utils.translation import gettext_lazy as _
from django import forms

# Member represents a team member
class Member(models.Model):
    
    #enum to represent different roles
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', _('Admin')
        REGULAR = 'REGULAR', _('Regular')
    
    #meta fields for a member
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=15, default='', unique=True)

    #set default role to Regular
    role = models.CharField(
        max_length=10,
        choices= Role.choices,
        default=Role.REGULAR,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name



