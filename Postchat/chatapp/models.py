from django.db import models

class myUser(models.Model):
    Name=models.CharField(max_length=25)
    Password=models.CharField(max_length=25)

class Post(models.Model):
    Name=models.CharField(max_length=25)
    comment=models.CharField(max_length=100)
    postData=models.ImageField(upload_to='post/images',blank=True,null=True)
   