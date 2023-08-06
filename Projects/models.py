from django.db import models
import os
from django.contrib.auth.models import User,Group
import uuid
import time
from auditlog.registry import auditlog
from datetime import datetime
#from thumbnails.fields import ImageField



def developer_photo_upload_to(instance, filename):
    return 'developer/photos/{filename}'.format(filename=filename)

class Developer(models.Model):
    Name = models.CharField(max_length=512, blank=True, null=True, default="")
    Logo = models.ImageField(default='default.jpg', upload_to='developer_photo_upload_to')
    Name = models.CharField(max_length=512, blank=True, null=True, default="")
    Bio = models.TextField(blank=True, null=True, default="")
    Address = models.CharField(max_length=512, blank=True, null=False)
    Mobile = models.CharField(max_length=16, blank=True, null=True, default="")
    Phone = models.CharField(max_length=16, blank=True, null=True, default="")

    Created = models.DateTimeField(auto_now_add=True)
    Modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name

auditlog.register(Developer)
auditlog.register(User)
auditlog.register(Group)