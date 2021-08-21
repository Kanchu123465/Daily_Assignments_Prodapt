from Donors.models import Donor
from django.shortcuts import render

# from Donors.models import Donor
from Donors.serializers import Donorserializers
from django.http import HttpResponse, response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.
def register(request):
    return render(request,'register.html')
    #####################
def bloodgroup(request):
    return render(request,'viewbloodg.html')
##############################

@csrf_exempt
def adddonor(request):
    if (request.method=='POST'):
        mydata=JSONParser().parse(request)
        donserial=Donorserializers(data=mydata)
        if(donserial.is_valid()):
            donserial.save()
            return response.JsonResponse(donserial.data)
        else:
            return HttpResponse("Validation fails")
    else:
        return HttpResponse("Post method not running")

####################
@csrf_exempt
def viewdonors(request):
    if(request.method=="GET"):
        donvar=Donor.objects.all()
        donserial=Donorserializers(donvar,many=True)
        return response.JsonResponse(donserial.data,safe=False)
    else:
        return HttpResponse("GET method not working")

############################
@csrf_exempt
def viewdetails(request,bloodg):
    try:
        donor=Donor.objects.get(bloodg=bloodg)
        if (request.method=="GET"):
            donserial=Donorserializers(donor)
            return response.JsonResponse(donserial.data,safe=False)
        if(request.method=="DELETE"):
            donor.delete()
            return HttpResponse("deleted")
        if(request.method=="PUT"):
            mynew=JSONParser().parse(request)
            donrserial=Donorserializers(data=mynew)
            if(donrserial.is_valid()):
                donrserial.save()
                return response.JsonResponse(donrserial.data)
            else:
                return HttpResponse("serialisation of new data fails")
    except Donor.DoesNotExist:
        return HttpResponse("Donor details not responding")

