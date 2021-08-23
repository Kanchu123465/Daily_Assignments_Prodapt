from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse
from django.http.response import JsonResponse

from donors.models import donors
from donors.serializer import donSerializer

# Create your views here.
@csrf_exempt
def adddon(request):
    if(request.method =='POST'):
        dondata = JSONParser().parse(request)
        don_serialize = donSerializer(data=dondata)

        if(don_serialize.is_valid()):
            don_serialize.save()
            return JsonResponse(don_serialize.data, status = status.HTTP_200_OK)

        else:
            return HttpResponse("Error in Serialization", status = status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("Welcome to add donor page!")

@csrf_exempt
def details(request, fetchid):
    try:
        don = donors.objects.get(bldgrp = fetchid)
        if (request.method == 'GET'):
            don_serialize = donSerializer(don)
            return JsonResponse(don_serialize.data, safe = False, status=status.HTTP_200_OK)
        if (request.method == "DELETE"):
                    don.delete()
                    return HttpResponse("Content Deleted", status=status.HTTP_204_NO_CONTENT)
        if(request.method =='PUT'):
             dondata = JSONParser().parse(request)
             don_serialize = donSerializer(don, data=dondata)
             if(don_serialize.is_valid()):
                 don_serialize.save()
                 return JsonResponse(don_serialize.data, status=status.HTTP_200_OK)

        
    except donors.DoesNotExist:
        return HttpResponse("Invalid ", status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def viewdon(request):
    if(request.method == 'GET'):
        don=donors.objects.all()
        don_serializer = donSerializer(don, many=True)
        return JsonResponse(don_serializer.data, safe=False)
        
    else:
        return HttpResponse("Welcome to view all donor details!")


def regdonors(request):
    return render(request, 'adddonor.html')


def searchdonors(request):
    return render(request, 'search.html')



