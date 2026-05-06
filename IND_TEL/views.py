from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hyderabad(request):
    return render(request,'hyd.html')

def warangal(request):
    response="<h1>welcome to warangal</h1>"
    return HttpResponse(response)

