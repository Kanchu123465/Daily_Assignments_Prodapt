from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from donar.serializers import DonarSerializer
from donar.models import donar
from rest_framework import status



# Create your views here.
def register_view(request):
    return render(request,'register.html')

def search_view(request):
    return render(request,'search.html')

@csrf_exempt
def adddonar(request):
    if(request.method=="POST"):
        mydict=JSONParser().parse(request)
        donar_serialize=DonarSerializer(data=mydict)
        if (donar_serialize.is_valid()):
            donar_serialize.save()
            return JsonResponse(donar_serialize.data)
        else:
            return HttpResponse("error in serilazation")

    else:
        return HttpResponse("SUCESSSSS")


@csrf_exempt
def viewdonar(request):
    if(request.method=="GET"):
        d1=donar.objects.all()
        donar_serializer=DonarSerializer(d1,many=True)
        return JsonResponse(donar_serializer.data,safe=False)


@csrf_exempt
def donarupdate(request,fetchid):
    try:
        d1=donar.objects.get(id=fetchid)
        if(request.method=="GET"):
            donar_serializer=DonarSerializer(d1)
            return JsonResponse(donar_serializer.data,safe=False)
        
        if(request.method=="PUT"):
            mydict=JSONParser().parse(request)
            donar_serialize=DonarSerializer(d1,data=mydict)
            if (donar_serialize.is_valid()):
                donar_serialize.save()
                return JsonResponse(donar_serialize.data)
            else:
                return JsonResponse(donar_serialize.errors)

                
        if(request.method=="DELETE"):
            d1.delete()
            return HttpResponse("Deleted".status=status)

    except donar.DoesNotExist:
        return HttpResponse("invalid syntax")

@csrf_exempt
def donarget(request,title):
    d2=donar.objects.get(bloodgroup=title)
    if(request.method=="GET"):
        donar_serializer=DonarSerializer(d2)
        return JsonResponse(donar_serializer.data,safe=False)


   