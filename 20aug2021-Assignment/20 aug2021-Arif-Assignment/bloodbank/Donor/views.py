from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from Donor.serializers import DoonSerializer
from Donor.models import Doon
from rest_framework.parsers import JSONParser
from rest_framework import status
def blood_register(request):
    return render(request,'register.html')

def blood_search(request):
    return render(request,'search.html')
@csrf_exempt
def blood_views(request):
    if (request.method=="POST"):
        mydata=JSONParser().parse(request)
        doon_serialize=DoonSerializer(data=mydata)
        
        if (doon_serialize.is_valid()):
            doon_serialize.save()
            return JsonResponse(doon_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def blood_vi(request):
    if(request.method=="GET"):
        k=Doon.objects.all()
        blood_serializer=DoonSerializer(k,many=True)
        return JsonResponse(blood_serializer.data,safe=False)

@csrf_exempt
def blood_single(request,fetchid):
    try:
        sh=Doon.objects.get(bloodgroup=fetchid)
    except Doon.DoesNotExist:
        return HttpResponse("invalid id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        blood_serialize=DoonSerializer(sh)
        return JsonResponse(blood_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        sh.delete()
        return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)
    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        blood_serialize=DoonSerializer(sh,data=mydata)

        if(blood_serialize.is_valid()):
            blood_serialize.save()
            return JsonResponse(blood_serialize.data,status=status.HTTP_200_OK)





