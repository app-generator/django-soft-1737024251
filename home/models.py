# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Formateurs(models.Model):

    #__Formateurs_FIELDS__
    nom = models.TextField(max_length=255, null=True, blank=True)
    prenom = models.TextField(max_length=255, null=True, blank=True)
    adresse = models.TextField(max_length=255, null=True, blank=True)
    date_naissance = models.TextField(max_length=255, null=True, blank=True)
    domaine = models.TextField(max_length=255, null=True, blank=True)
    diplomes = models.TextField(max_length=255, null=True, blank=True)

    #__Formateurs_FIELDS__END

    class Meta:
        verbose_name        = _("Formateurs")
        verbose_name_plural = _("Formateurs")



#__MODELS__END
