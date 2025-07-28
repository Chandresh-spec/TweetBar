from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

created_at = models.DateTimeField(auto_now_add=True)


# Create your models here.


class Tweet(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
      tweet=models.TextField(null=True,blank=True)
      image=models.ImageField(upload_to='photos/',null=True)
      created_at = models.DateTimeField(default=timezone.now)


      def __str__(self):
          return self.tweet