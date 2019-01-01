from django.shortcuts import render
from django.http import HttpResponse
from kick.models import KickstarterTypes
from django.http import JsonResponse
from django.core import serializers

def index(request):
    return HttpResponse("Now to get the data. " + str(KickstarterTypes.objects.all()[int(1)].backers_count) + " <--")

def id_request(request,id_num):
    #return HttpResponse("Should be data: " + str(KickstarterTypes.objects.all()[int(id_num)].backers_count) + " <--")
    return JsonResponse(serializers.serialize('json', [ KickstarterTypes.objects.all()[id_num], ]), safe=False)

