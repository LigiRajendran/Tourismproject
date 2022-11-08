from django.db import models
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()



class Team(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    def __str__(self):
      return self.name