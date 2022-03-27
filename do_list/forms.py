from dataclasses import field
from django import forms
from .models import List_Mission
class List_MissionForms(forms.ModelForm):
  
    name = forms.CharField(max_length=200,label='اسم المهمه',widget=forms.TextInput())
    time_mission = forms.TimeField(label='وقت المهمه',widget=forms.TimeInput(attrs={'type':'time'}))
    day_mission = forms.DateField(label='يوم المهمه',widget=forms.DateInput(attrs={'type':'date'}))
    finish_mission = forms.BooleanField(required=False,label="انتهاء المهمه")

    class Meta:
        model=List_Mission
        fields='__all__'
     
