from django.shortcuts import render
from donor.models import Donor
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from donor.serializers import DonorSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.
def donor_view(request):
    return render(request,'register.html') 
def donor_view(request):
    return render(request,'search.html') 
@csrf_exempt
def donor_details(request,bloodgroup):
    try:
        donors=Donor.objects.get(bloodgroup=bloodgroup)
        if(request.method=="GET"):
            donor_serializer=DonorSerializer(donors)
            return JsonResponse(donor_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            donors.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            donor_serialize=DonorSerializer(donors,data=mydata)
            if(donor_serialize.is_valid()):
                donor_serialize.save()
                return JsonResponse(donor_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(donor_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Donor.DoesNotExist:
        return HttpResponse("Invalid BloodGroup",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def donor_list(request):
    if(request.method=="GET"):
        donors=Donor.objects.all()
        donor_serializer=DonorSerializer(donors,many=True)
        return JsonResponse(donor_serializer.data,safe=False)
@csrf_exempt
def donor_create(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
       
        donor_serialize=DonorSerializer(data=mydata)
        if(donor_serialize.is_valid()):
            donor_serialize.save()
            return JsonResponse(donor_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Get Method Not Allowed",status=status.HTTP_404_NOT_FOUND)





