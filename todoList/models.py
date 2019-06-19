from django.db import models
from django.utils.timezone   import datetime

# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=100)
    desc  = models.TextField()
    update_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title