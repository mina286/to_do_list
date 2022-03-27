from multiprocessing import context
from django.shortcuts import redirect, render,get_object_or_404
from .forms import List_MissionForms
from django.contrib import  messages
from .models import List_Mission
# Create your views here.
def add_missions(request):
    context=None
    n=None
    list_missionforms= List_MissionForms()
    missions=List_Mission.objects.all()

    if request.method == 'GET' and 'btn_addd' in request.GET:
        list_missionforms= List_MissionForms(request.GET)

        if list_missionforms.is_valid():
            list_missionforms.save()
            messages.success(request,'success add mission')
        else:
            messages.error(request,'form not valid please')
        n=request.GET['name']
    context = {
                'list_missionforms':list_missionforms,
                'missions':missions,
                'n':n
        }
    return render(request,'do_list/missions.html',context)
#########################
def active_mission(request):
    if request.method == 'GET' and 'ch' in request.GET and 'fromch' in request.GET:
        id_mission=request.GET['id_miss']
        mission=List_Mission.objects.get(id=id_mission)
        mission.finish_mission=True
        mission.save()


    if request.method == 'GET'  and not 'ch' in request.GET and 'fromch' in request.GET:
        id_mission=request.GET['id_miss']
        mission=List_Mission.objects.get(id=id_mission)
        mission.finish_mission=False
        mission.save()


    list_missionforms= List_MissionForms()
    missions=List_Mission.objects.all() 
    context = {
                'list_missionforms':list_missionforms,
                'missions':missions,
        }
    return render(request,'do_list/missions.html',context)

###############
def del_mission(request,id_mission):
    mission=List_Mission.objects.get(id=id_mission)
    mission.delete()

    list_missionforms= List_MissionForms()
    missions=List_Mission.objects.all() 
    context = {
                'list_missionforms':list_missionforms,
                'missions':missions,
        }
    return render(request,'do_list/missions.html',context)
#################
def show(request,id_mission):
    mission=List_Mission.objects.get(id=id_mission)

    context = {
                'mission':mission,
        }
    return render(request,'do_list/show.html',context)