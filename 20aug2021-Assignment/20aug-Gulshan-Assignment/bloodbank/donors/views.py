from codecs import StreamReader
import donors
from donors.serializers import BloodSerializer
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import HttpResponse,JsonResponse
from donors.models import Blood
# Create your views here.

def add_donor(request):
    return render(request,'index.html')

def search(request):
    return render(request,'searchindex.html')
@csrf_exempt
def doner_list(request):
    if(request.method == "GET"):
        donor = Blood.objects.all()
        donor_serialize=BloodSerializer(donor,many = True)
        return JsonResponse(donor_serialize.data,safe=False)


@csrf_exempt 
def doner_update(request,id):
    try:
        donor=Blood.objects.get(id=id)
        if(request.method == "GET"):
            doner_serialize=BloodSerializer(donor)
            return JsonResponse(doner_serialize.data,safe=False)
        
        if (request.method =="DELETE"):
            donor.delete()
            return HttpResponse("Data is deleted")
        if (request.method == "PUT"):
            blood_data = JSONParser().parse(request)
            blood_serialize  =BloodSerializer(donor,data=blood_data)
            if (blood_serialize.is_valid()):
                blood_serialize.save()
                return JsonResponse(blood_serialize.data)
            else:
                return HttpResponse("error in serialization")
    except Blood.DoesNotExist:
        return HttpResponse("Given id is invailed")


@csrf_exempt
def add(request):
    if (request.method == "POST"):
        blood_data = JSONParser().parse(request)
        blood_serialize = BloodSerializer(data=blood_data)
        if(blood_serialize.is_valid()):
            blood_serialize.save()
            return JsonResponse(blood_serialize.data)
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error in serialization ")
    
