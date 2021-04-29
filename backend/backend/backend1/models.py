from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#class Category(models.Model):
 #   name = models.CharField(max_length=100)
#
  #  def __str__(self):
   #     return self.name

class data(models.Model):

    #category = models.ForeignKey(
      #  Category, on_delete=models.PROTECT, default=1 )
    weight = models.IntegerField()
    calories_in = models.IntegerField()
    calories_out = models.IntegerField()
    heartrate = models.IntegerField()
    fat = models.IntegerField()
    carbs = models.IntegerField()
    protein = models.IntegerField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='info')
    objects = models.Manager()


    
    
    

    