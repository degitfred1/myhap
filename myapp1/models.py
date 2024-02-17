from django.db import models

class music(models.Model):
      title=models.CharField(max_length=20)
      time=models.DateTimeField(auto_now_add=True)

class mark(models.Model):
      num=models.IntegerField()
      post=models.CharField(max_length=30)



class box(models.Model):
      name=models.ForeignKey(music,on_delete=models.CASCADE) 

