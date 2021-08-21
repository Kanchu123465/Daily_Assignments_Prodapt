from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from donor.serializers import DonorSerializer
from donor.models import Donor
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
def register(request):
    return render(request,'register.html')
def search(request):
    return render(request,'search.html')

@csrf_exempt
def donor_details(request,bgroup):
    try:
        donor=Donor.objects.get(blood_group=bgroup)
        if(request.method=="GET"):
            donor_serializer=DonorSerializer(donor)
            return JsonResponse(donor_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            donor.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            donor_serializer=DonorSerializer(donor,data=mydata)
            if(donor_serializer.is_valid()):
                donor_serializer.save()  
                return JsonResponse(donor_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(donor_serializer.errors,status=status.HTTP_400_BAD_REQUEST)        
    except donor.DoesNotExist:
        return HttpResponse("Invalid BLOOD GROUP ",status=status.HTTP_404_PAGE_NOT_FOUND)    

@csrf_exempt
def donor_list(request):
    if(request.method=="GET"):
        donor=Donor.objects.all()
        donor_serializer=DonorSerializer(donor,many=True)
        return JsonResponse(donor_serializer.data,safe=False)       

@csrf_exempt
def donoraddpage(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        donor_serialize=DonorSerializer(data=mydata)
        if(donor_serialize.is_valid()):
            donor_serialize.save()
            return JsonResponse(donor_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST) 
    else:
        return HttpResponse("No get method allowed",status=status.HTTP_404_PAGE_NOT_FOUND)                   