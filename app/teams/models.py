from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=200)
    subdomain = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
