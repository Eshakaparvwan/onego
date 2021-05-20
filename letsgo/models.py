from django.db import models
from django.conf import settings
# Create your models here.

class User_details(models.Model):
    user_name=models.CharField(max_length=30,default="")
    page_id=models.IntegerField(default=0)
    access_token=models.CharField(max_length=20000000000,default="")
    
    def __str__(self):
        return self.user_name