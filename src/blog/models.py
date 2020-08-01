from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.TextField(default='wow')
    description = models.TextField(default='this is cool!')
    summary = models.TextField(default='amazing')
