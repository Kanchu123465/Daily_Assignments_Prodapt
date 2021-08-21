from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from donors.serializer import DonorSerializer
from donors.models import Donors
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.

def regi(request):
    return render(request,'registration.html')
def search(request):
    return render(request,'search.html')

@csrf_exempt
def add(request):
    if(request.method == "POST"):
        mydata = JSONParser().parse(request)
        donor_serializer = DonorSerializer(data=mydata)
        if(donor_serializer.is_valid()):
            donor_serializer.save()
            return JsonResponse(donor_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("GET method not allowed",status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def viewall(request):
    if(request.method == "GET"):
        donors = Donors.objects.all()
        donor_serializer = DonorSerializer(donors,many=True)
        return JsonResponse(donor_serializer.data,safe=False)
@csrf_exempt
def view_one(request,fetchid):
    try:
        donors = Donors.objects.get(blood_group=fetchid)
    except Donors.DoesNotExist:
        return JsonResponse("iNVALID id",status=status.HTTP_404_NOT_FOUND)
    if(request.method == "GET"):
        donor_seriaizer = DonorSerializer(donors)
        return JsonResponse(donor_seriaizer.data,status=status.HTTP_201_CREATED)
    if(request.method == "PUT"):
        mydata = JSONParser().parse(request)
        donor_seriaizer = DonorSerializer(donors,data=mydata)
        if(donor_seriaizer.is_valid()):
            donor_seriaizer.save()
            return JsonResponse(donor_seriaizer.data,status=status.HTTP_201_CREATED)
        else:
            return HttpResponse("Erroe in serilaizer",status=status.HTTP_404_NOT_FOUND)
    if(request.method == "DELETE"):
        donors.delete()
        return HttpResponse("Deleted item",status=status.HTTP_204_NO_CONTENT)
    
