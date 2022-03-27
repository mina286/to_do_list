from os import name
from django.urls import path
from . import views
urlpatterns = [
    path('',views.add_missions,name="add_missions"),
    path('active_mission',views.active_mission,name="active_mission"),
    path('del_mission/<int:id_mission>',views.del_mission,name="del_mission"),
    path('show/<int:id_mission>',views.show,name="show"),


]
