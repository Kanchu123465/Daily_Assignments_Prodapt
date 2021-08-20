from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from donar.serializers import DonarSerializer
from donar.models import Donar
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.

def registerdonar(request):
    return render(request,"index.html")


def searchdonar(request):
    return render(request,"search.html")



@csrf_exempt
def adddonar(request):
    if(request.method=="POST"):
        
        mydict=JSONParser().parse(request)
        donar_serialize=DonarSerializer(data=mydict)
        if (donar_serialize.is_valid()):
            donar_serialize.save()
            return JsonResponse(donar_serialize.data,status=status.HTTP_200_OK)
        
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
      
    else:
        return HttpResponse("no get method allowed",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def donar_list(request):
    if(request.method=="GET"):
        donars=Donar.objects.all()
        donar_serializer=DonarSerializer(donars,many=True)
        return JsonResponse(donar_serializer.data,safe=False)
        
@csrf_exempt
def donar_details(request, bloodgroup):
    try:
        donars=Donar.objects.get(bloodgroup=bloodgroup)
    except Donar.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        donar_serializer=DonarSerializer(donars)
        return JsonResponse(donar_serializer.data,safe=False,status=status.HTTP_200_OK)

    if(request.method=="DELETE"):
        donars.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT) 

    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        donar_serialize=DonarSerializer(donars,data=mydict)
        if (donar_serialize.is_valid()):
            donar_serialize.save()
            return JsonResponse(donar_serialize.data,status=status.HTTP_200_OK)
            