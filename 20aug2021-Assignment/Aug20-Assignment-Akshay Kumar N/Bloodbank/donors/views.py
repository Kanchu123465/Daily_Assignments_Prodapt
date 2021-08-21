from donors.serializers import DonorSerializers
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from donors.models import Donors


def registerDonor(request):
    return render(request,'register.html')

def search(request):
    return render(request,'view.html')

@csrf_exempt
def addDonor(request):
    if(request.method == "POST"):
        mydata = JSONParser().parse(request)
        donor_s = DonorSerializers(data = mydata )
        if(donor_s.is_valid()):
            donor_s.save()
            return JsonResponse(donor_s.data)
        else:
            return HttpResponse("Error in Serialization")
    else:
        return HttpResponse("GET Method not allowed")

@csrf_exempt
def viewDonors(request):
    if(request.method == "GET"):
        donor= Donors.objects.all()
        d_serializer = DonorSerializers(donor, many=True)
        return JsonResponse(d_serializer.data, safe=False) 
         
@csrf_exempt
def donorsData(request,bgroup):
    try:
        donor = Donors.objects.get(bgroup = bgroup)
        if(request.method == "GET"):
            d_serialize = DonorSerializers(donor)
            return JsonResponse(d_serialize.data, safe=False)

        if (request.method == "DELETE"):
            donor.delete()
            return HttpResponse("Deleted")

        if(request.method == "PUT"):
            donorss = JSONParser().parse(request)
            dd = DonorSerializers(donor, data = donorss  )
            if(dd.is_valid()):
                dd.save()
                return JsonResponse(dd.data)

    except Donors.DoesNotExist:
        return HttpResponse("Invalid Donors ID")        