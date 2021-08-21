import donors
from django.shortcuts import render
from donors.models import Donors
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from donors.serializers import DonorsSerializer
from rest_framework.parsers import JSONParser

# Create your views here.
def myRegister(request):
    return render(request,'register.html')

def mySearch(request):
    return render(request,'search.html')


@csrf_exempt
def myDonorsDetails(request,bloodgroup):
    try:
        donor=Donors.objects.get(bloodgroup=bloodgroup)
        if(request.method=="GET"):
            donors_serializer=DonorsSerializer(donor)
            return JsonResponse(donors_serializer.data,safe=False)
        if(request.method=="DELETE"):
            donor.delete()
            return HttpResponse("Deleted")
        if(request.method=="PUT"):
            dict=JSONParser().parse(request)
            donors_serialize=DonorsSerializer(data=dict)
            if(donors_serialize.is_valid()):
                donors_serialize.save()
                return JsonResponse(donors_serialize.data)
            else:
                return JsonResponse(donors_serialize.errors)
    except Donors.DoesNotExist:
        return HttpResponse("Invalid")


@csrf_exempt
def myDonorsPage(request):
    if(request.method=="POST"):
        dict=JSONParser().parse(request)
        donors_serialize=DonorsSerializer(data=dict)
        if(donors_serialize.is_valid()):
            donors_serialize.save()
            return JsonResponse(donors_serialize.data)
        else:
            return HttpResponse("Error in Serialization")
    else:
        return HttpResponse("Get method is not allowed")

@csrf_exempt
def myDonorsList(request):
    if(request.method=="GET"):
        donor=Donors.objects.all()
        donors_serializer=DonorsSerializer(donor,many=True)
        return JsonResponse(donors_serializer.data,safe=False)