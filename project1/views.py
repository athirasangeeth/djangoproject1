from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def samplefunction(request):
    return HttpResponse("Welcome")
def testfunction(request):
        return render(request,'athira.html')
def formfunction(request):
    return render(request,'Form.html')