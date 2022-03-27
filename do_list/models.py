from tabnanny import verbose
from django.db import models
from django.shortcuts import render

# Create your models here.
class List_Mission(models.Model):
    name = models.CharField(max_length=200,verbose_name='اسم المهمه')
    time_mission = models.TimeField(verbose_name='وقت المهمه')
    day_mission = models.DateField(verbose_name='يوم المهمه')
    finish_mission = models.BooleanField(default=False,verbose_name='انتهاء المهمه',null=True,blank=True)
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name