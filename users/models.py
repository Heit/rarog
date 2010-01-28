#coding: utf-8 
from django.db import models
from django.contrib.auth.models import User, UserManager
from photologue.models import Photo
from django.utils.translation import ugettext as _

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='profile')
    timezone = models.CharField(max_length=50, default='Europe/Moskow')
    objects = UserManager()
    photo = models.ForeignKey(Photo, blank=True, null=True)
    seat = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('-user',)
        verbose_name = (_('userprofile'))
        verbose_name_plural = (_('userprofiles'))


