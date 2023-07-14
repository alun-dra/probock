from django.db import models
from .range import Range

class User(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)
    profession = models.CharField(max_length=100, blank=False, null=False)
    job_position = models.CharField(max_length=100, blank=False, null=False)
    range_id = models.ForeignKey(Range, on_delete=models.SET_NULL, null=True, blank=False, related_name='users')

    def __str__(self):
        return self.name
