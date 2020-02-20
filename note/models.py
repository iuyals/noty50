from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    title=models.CharField(max_length=16)
    content=models.CharField(max_length=1024)
    level=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="notes")

    def __str__(self):
        return f"{self.level} {self.user} {self.title}+{self.content}"