from django.db import models
from django.utils import timezone


class equipList(models.Model):
    tag = models.CharField(max_length=30)
    identification = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    link = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.tag
