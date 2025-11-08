from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.


def sample(request):
    return HttpResponse('hello world')

def sample1(request):
    return HttpResponse('wellcome Django')

def sampleInfo(request):
    data={"name":"sneha","age":21,"city":"hyb"}
    return JsonResponse(data)  

def sample2(request):
    data1=[1,2,34,7,5,0]
    return JsonResponse(data1,safe=False) 

def dynamicResponse(request):
    name=request.GET.get("name",'')
    city=request.GET.get("city","hyb") 
    return HttpResponse(f"hello{name} from {city}")       