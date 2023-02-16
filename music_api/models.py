from datetime import datetime
from django.db import models
from .song_upload import upload_to

class Music(models.Model):
    song = models.FileField(upload_to=upload_to,blank = True,null=True)
    creation_date = models.DateTimeField(default=datetime.now())
    
    
