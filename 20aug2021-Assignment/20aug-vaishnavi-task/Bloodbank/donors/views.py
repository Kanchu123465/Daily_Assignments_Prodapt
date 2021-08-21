from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from donors.serializer import DonorSerializer
from django.http.response import JsonResponse
from django.http.response import HttpResponse
from donors.models import Donorapp1


def register(request):
    return render(request,'register.html')

def search(request):
    return render(request,'search.html')


@csrf_exempt
def donor(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        Donor_Serializer= DonorSerializer(data=mydata)
        if(Donor_Serializer.is_valid()):
            Donor_Serializer.save()
            return JsonResponse(Donor_Serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No get method",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def donor_list(request):
    if(request.method == "GET"):
        donors = Donorapp1.objects.all()
        Donor_Serializer= DonorSerializer(donors, many=True)
        return JsonResponse(Donor_Serializer.data, safe=False)


@csrf_exempt
def donordetail(request,id):
    try:
        donors=Donorapp1.objects.get(bloodgroup=id)
        if(request.method == "GET"):
            Donor_Serializer=DonorSerializer(donors)
            return JsonResponse(Donor_Serializer.data, safe=False, status=status.HTTP_200_OK)

        if(request.method=="DELETE"):
            donors.delete()
            return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)

        if(request.method == "PUT"):
            mydata=JSONParser().parse(request)
            Donor_Serializer = DonorSerializer(donors,data=mydata)
            if(Donor_Serializer.is_valid()):
                Donor_Serializer.save()
                return JsonResponse(Donor_Serializer.data,status=status.HTTP_200_OK)

            else:
                return HttpResponse("Error in serialization")

    except Donorapp1.DoesNotExist:
        return HttpResponse("Invalid donor bloodgroup",status=status.HTTP_404_NOT_FOUND)
