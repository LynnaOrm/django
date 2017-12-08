from __future__ import unicode_literals
from django.db import models
from ..belt_exam4.models import User
from datetime import datetime


class QuoteManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['quoted_by']) < 3:
            errors["Quoted by name must be at least 3 characters"] = "Quoted by name must be at least 3 characters"

        if len(postData['message']) < 10:
            errors["Message must be at least 10 characters"] = "Message must be at least 10 characters"

        return errors


class Quote(models.Model):
    quoted_by = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    posted_by = models.ForeignKey(User, related_name='quotes')
    favorited_by = models.ManyToManyField(User, related_name='favorites')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()

