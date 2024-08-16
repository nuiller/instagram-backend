from django.db import models




class Users(models.Model):
    username = models.CharField(max_length=256,verbose_name="Username")
    password = models.CharField(max_length=256,verbose_name="Password")

    create_at = models.DateField(auto_now=True,blank=True)