from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from donorapp.models import Donor
from donorapp.serializers import DonorSerializers
from django.views.decorators.csrf import csrf_exempt

def registerDonor(request):
    return render(request,'registerdonor.html')

def searchDonor(request):
    return render(request,'searchdonor.html')

@csrf_exempt
def add_donor_api(request):
    if(request.method=='POST'):
        mydata=JSONParser().parse(request)
        donor_serialize=DonorSerializers(data=mydata)
        if(donor_serialize.is_valid()):
            donor_serialize.save()
            return JsonResponse(donor_serialize.data)
        else:
            return HttpResponse("Error in serialization")
    else:
        return HttpResponse("no GET method is allowed")

@csrf_exempt
def show_donor_api(request):
    if(request.method=='GET'):
        d1=Donor.objects.all()
        donor_serialize=DonorSerializers(d1,many=True)
        return JsonResponse(donor_serialize.data,safe=False)

@csrf_exempt
def show_a_donor_api(request,bloodgroup):
    try:
        d1=Donor.objects.get(bloodgroup=bloodgroup)
    except Donor.DoesNotExist:
        return HttpResponse("Invalid blood group")

    if(request.method=='GET'):
        donor_serialize=DonorSerializers(d1)
        return JsonResponse(donor_serialize.data,safe=False)

    if(request.method=='PUT'):
        
        mydata=JSONParser().parse(request)
        donor_serialize=DonorSerializers(d1,data=mydata)
        if(donor_serialize.is_valid()):
            donor_serialize.save()
            return JsonResponse(donor_serialize.data)
        
        else:
            return HttpResponse("something went wrong ")

    if(request.method=='DELETE'):
        d1.delete()
        return HttpResponse("Donor deleted")

