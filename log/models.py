from django.db import models
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.humanize.templatetags.humanize import naturaltime

class Activity(models.Model):
    class Meta:
        verbose_name_plural = "Activities"
        
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name

class Log(models.Model):
    class Meta: 
        ordering = ['-timestamp']
    
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now)
    remark = models.CharField(max_length=1024, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    
    @property
    def when(self):
        return naturaltime(self.timestamp)
