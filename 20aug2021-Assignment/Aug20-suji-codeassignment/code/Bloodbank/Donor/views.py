from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from Donor.serializers import DonorSerializer
from Donor.models import Donor1
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
def donors(request):
    return render(request,'register.html')
def search(request):
    return render(request,'search.html')  

@csrf_exempt
def donor_list(request):
    if(request.method=="GET"):
        donors=Donor1.objects.all()
        donor_serialize=DonorSerializer(donors,many=True)
        return JsonResponse(donor_serialize.data,safe=False)    

@csrf_exempt
def donor_details(request,fetchid):
    try:
        donors=Donor1.objects.get(id=fetchid)
    except Donor1.DoesNotExist:
        return HttpResponse("Invalid donor Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        donor_serialize=DonorSerializer(donors)
        return JsonResponse(donor_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        donors.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)   

    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        donor_serialize=DonorSerializer(donors,data=mydict)
        if(donor_serialize.is_valid()):
            donor_serialize.save()
            return JsonResponse(donor_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(donor_serialize.errors,status=status.HTTP_400_BAD_REQUEST)    

@csrf_exempt
def donor_add(request):
    if request.method=="POST":
        getName=request.POST.get("name")
        getAddress=request.POST.get("address")
        getBloodgroup=request.POST.get("bloodgroup")
        getMobilenumber=request.POST.get("mobileno")
        getLastdonateddate=request.POST.get("lastdonateddate")
        getPincode=request.POST.get("pincode")
        mydict={"name":getName,"address":getAddress,"bloodgroup":getBloodgroup,"mobileno":getMobilenumber,"lastdonateddate":getLastdonateddate,"pincode":getPincode};
        mydata=JSONParser().parse(request)
        donor_serialize=DonorSerializer(data=mydict)
        if(donor_serialize.is_valid()):
            donor_serialize.save()
            return JsonResponse(donor_serialize.data,status=status.HTTP_200_OK)
            #return HttpResponse("Success")
            #result=json.dumps(mydict)
            #return HttpResponse(result)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)    
    else:
        return HttpResponse("No get method allowed",status=status.HTTP_404_NOT_FOUND)
   
