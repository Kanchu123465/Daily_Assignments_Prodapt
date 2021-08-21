from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from Donar.serializers import donarSerializer
from Donar.models import Donar
from rest_framework.parsers import JSONParser
from rest_framework import status 
# Create your views here.

def register(request):
    return render(request,"register.html")

def search(request):
    return render(request,"search.html")


@csrf_exempt
def donar(request):
    if(request.method=="POST"):
        mydic=JSONParser().parse(request)
        donar_serialize=donarSerializer(data=mydic)
        if (donar_serialize.is_valid()):
            donar_serialize.save()
            return JsonResponse(donar_serialize.data)
        else:
            return HttpResponse("error in serilazation")

    else:
        return HttpResponse("sucess")


@csrf_exempt
def donarlist(request):
    if(request.method=="GET"):
        donars=Donar.objects.all()
        donar_serializer=donarSerializer(donars,many=True)
        return JsonResponse(donar_serializer.data,safe=False)

@csrf_exempt
def mydonars(request,fetchgroup):
    try:
        donar1=Donar.objects.get(bloodgroup=fetchgroup)
        if(request.method=="GET"):
            donar_serializer=donarSerializer(donar1)
            return JsonResponse(donar_serializer.data,safe=False)

        if(request.method=="DELETE"):
            donar1.delete()
            return HttpResponse("Deleted",status=status)

        if(request.method=="PUT"):
            mydic=JSONParser().parse(request)
            donar_serialize=donarSerializer(donar1,data=mydic)
            if (donar_serialize.is_valid()):
                donar_serialize.save()
                return JsonResponse(donar_serialize.data)
            else:
                return JsonResponse(donar_serialize.errors)
    except donar.DoesNotExist:
        return HttpResponse("invalid syntax")