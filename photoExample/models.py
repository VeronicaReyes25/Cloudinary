from django.db import models
from django.utils import timezone

class photoExample(models.Model):
        url = models.TextField()
        created_date = models.DateTimeField(
                default=timezone.now)
        
        def __str__(self):
            return self.title