from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    summary = models.TextField(default='')
